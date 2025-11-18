import base64
import requests
import os
import time
import json
import fitz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import urlparse



def read_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    return data



# -----------------------
# Helpers: GitHub API (upload/get sha)
# -----------------------
def _github_headers(token):
    return {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}


def github_get_file_sha(repo, path, branch, token):
    """Return sha if file exists, else None"""
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"
    r = requests.get(url, headers=_github_headers(token))
    if r.status_code == 200:
        return r.json().get("sha")
    return None



def github_upload(repo, branch, token, filepath, dest_path):
    import base64
    import requests

    api_url = f"https://api.github.com/repos/{repo}/contents/{dest_path}"
    headers = {"Authorization": f"token {token}"}

    # ❗ Check if file exists ON THE TARGET BRANCH
    r = requests.get(api_url, headers=headers, params={"ref": branch})
    sha = None
    if r.status_code == 200:
        sha = r.json().get("sha")
    elif r.status_code == 404:
        sha = None
    else:
        raise Exception(f"Unexpected GitHub response {r.status_code}: {r.text}")

    # Encode file
    with open(filepath, "rb") as f:
        content_b64 = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "message": f"Upload {dest_path}",
        "content": content_b64,
        "branch": branch
    }

    # Only include sha when overwriting
    if sha:
        payload["sha"] = sha

    put = requests.put(api_url, headers=headers, json=payload)

    if put.status_code not in (200, 201):
        raise Exception(f"GitHub upload failed {put.status_code}: {put.text}")

    return put.json()["content"]["download_url"]




# -----------------------
# Split & ensure under 1024KB (PyMuPDF-only)
# -----------------------
def split_pdf_into_pages_under_limit(input_pdf, output_dir='split_pages', max_kb=1024):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(input_pdf)
    total = doc.page_count
    page_pdf_paths = []

    for i in range(total):
        out_path = os.path.join(output_dir, f"page_{i+1:03}.pdf")
        one = fitz.open()
        one.insert_pdf(doc, from_page=i, to_page=i)
        one.save(out_path)
        one.close()

        # compress if needed
        if os.path.getsize(out_path) > max_kb * 1024:
            out_path = _compress_until_under_limit(out_path, max_kb)
        page_pdf_paths.append(out_path)

    doc.close()
    return page_pdf_paths


def _compress_until_under_limit(pdf_path, max_kb):
    """
    Attempt to compress the given one-page PDF using PyMuPDF's save options.
    Stops if no improvement.
    """
    attempt = 0
    while os.path.getsize(pdf_path) > max_kb * 1024 and attempt < 5:
        attempt += 1
        doc = fitz.open(pdf_path)
        compressed = pdf_path.replace(".pdf", f"_cmp{attempt}.pdf")
        # deflate, clean, garbage: will often reduce size
        doc.save(compressed, deflate=True, clean=True, garbage=4)
        doc.close()
        if os.path.getsize(compressed) < os.path.getsize(pdf_path):
            os.remove(pdf_path)
            os.rename(compressed, pdf_path)
        else:
            os.remove(compressed)
            break
    return pdf_path


# -----------------------
# Render page to PNG (Poppler-free, PyMuPDF)
# -----------------------
def render_pdf_page_to_png(pdf_path, out_dir, zoom=2.0):
    """
    Render page_index (0-based) of pdf_path to PNG and return local image path.
    """
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)  # page PDF is single-page file, so load_page(0)
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    img_name = f"{os.path.splitext(os.path.basename(pdf_path))[0]}.png"  # e.g., page_001.png
    out_path = os.path.join(out_dir, img_name)
    pix.save(out_path)
    doc.close()
    return out_path


# -----------------------
# Text extraction: prefer digital text, else OCR.space on image
# -----------------------
def extract_text_from_single_page_pdf(page_pdf_path, ocr_api_key):
    # Try digital selectable text first
    doc = fitz.open(page_pdf_path)
    page = doc.load_page(0)
    text = page.get_text("text").strip()
    doc.close()
    if text and len(text.split()) > 3:
        return text  # prefer directly extracted digital text

    # else render an image and call OCR.space
    img_path = render_pdf_page_to_png(page_pdf_path, os.path.join('split_pages/images'))
    try:
        ocr_text = ocr_space_image(img_path, api_key=ocr_api_key)
    finally:
        # keep the image for upload; do not remove here
        pass
    return ocr_text or ""


def ocr_space_image(image_path, api_key):
    """Call OCR.space with an image file; returns extracted text or ''."""
    url = "https://api.ocr.space/parse/image"
    with open(image_path, "rb") as f:
        r = requests.post(url, files={"file": f}, data={"apikey": api_key, "OCREngine": 2, "isOverlayRequired": False})
    try:
        j = r.json()
    except Exception:
        print("OCR.space returned non-json or failed.")
        return ""
    parsed = ""
    if j.get("ParsedResults"):
        for pr in j["ParsedResults"]:
            parsed += pr.get("ParsedText", "")
    return parsed


# ---------------
# Main pipeline
# ---------------
def pdf_to_markdown_with_github(input_pdf, api_key, repo, branch, token, output_md,
                                         images_remote_folder, outputs_remote_folder):
    """
    Full pipeline:
      - split into one-page PDFs under 1024KB
      - for each page: render PNG, extract text (digital/OCR), upload PNG to GitHub images/
      - assemble single markdown containing image URL + text per page
      - upload markdown to GitHub outputs/
    Returns: dict with local output_md, remote_md_url (raw), and list of image URLs
    """
    # 1) split pages
    page_pdfs = split_pdf_into_pages_under_limit(input_pdf)
    md_blocks = []
    image_urls = []

    for idx, page_pdf in enumerate(page_pdfs, start=1):
        print(f"\nProcessing page {idx}/{len(page_pdfs)} -> {page_pdf}")

        # 2) ensure we have a PNG screenshot (render from single-page PDF)
        png_local = render_pdf_page_to_png(page_pdf, os.path.join('split_pages/images'))

        # 3) upload PNG to repo under images_remote_folder
        remote_image_path = f"{images_remote_folder}/{os.path.basename(png_local)}"
        img_url = github_upload_with_retries(png_local, repo, remote_image_path, branch, token)
        if not img_url:
            print(f"Failed to upload image for page {idx}, continuing.")
        else:
            image_urls.append(img_url)

        # 4) extract text (digital preferred, else OCR.space)
        text = extract_text_from_single_page_pdf(page_pdf, api_key)
        if not text:
            text = "*No text found on this page.*"

        # 5) assemble markdown block (image first)
        if img_url:
            md = f"## Page {idx}\n\n![Page {idx}]({img_url})\n\n{text}\n\n"
        else:
            md = f"## Page {idx}\n\n{text}\n\n"
        md_blocks.append(md)

        # cleanup local page_pdf and png
        try:
            os.remove(page_pdf)
        except OSError:
            pass
        try:
            os.remove(png_local)
        except OSError:
            pass

    # 6) write local output md
    full_md = "\n".join(md_blocks)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"\nLocal Markdown written: {output_md}")

    # 7) upload markdown to repo under outputs_remote_folder
    remote_md_path = f"{outputs_remote_folder}/{os.path.basename(output_md)}"
    md_url = github_upload_with_retries(output_md, repo, remote_md_path, branch, token)
    if not md_url:
        print("Failed to upload Markdown to GitHub.")
    else:
        print("Uploaded Markdown to GitHub:", md_url)

    return {"local_md": output_md, "remote_md_url": md_url, "image_urls": image_urls}


# -----------------------
# Small wrapper adding retries for GitHub uploads
# -----------------------
def github_upload_with_retries(local_path, repo, remote_path, branch, token, retries=3, backoff=1.0):
    for attempt in range(1, retries + 1):
        url = github_upload(repo, branch, token, local_path, remote_path)
        if url:
            return url
        else:
            wait = backoff * attempt
            print(f"Retry {attempt}/{retries} after {wait:.1f}s...")
            time.sleep(wait)
    return None




if __name__ == '__main__':
    config_dict = read_json('config.json')
    API_KEY = config_dict['API_KEY']
    REPO = 'qinshirl/SkuleBot'
    BRANCH = 'shifang'
    TOKEN = config_dict['GitHub_Token']
    print(API_KEY)
    print(TOKEN)

    json_file_list = ['ECE110H1.json']
    for path in json_file_list:
        data_dict = read_json(path)
        for key in data_dict:
            OUTPUT_FOLDER = path.replace('.json', '') + ' ---- ' + key
            os.makedirs(OUTPUT_FOLDER, exist_ok=True)
            for pdf_file_url in data_dict[key]:
                # 1. Launch Selenium browser
                # if pdf_file_url == "https://courses.skule.ca/course/APS100H1#20259":
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver.get(pdf_file_url)
                driver.implicitly_wait(5)

                # --- CLICK EVERYTHING THAT CAN REVEAL CONTENT ---

                # click buttons
                buttons = driver.find_elements(By.TAG_NAME, "button")
                for b in buttons:
                    try:
                        driver.execute_script("arguments[0].click();", b)
                    except:
                        pass

                # click elements that expand on click (e.g., divs with JS)
                clickables = driver.find_elements(By.XPATH, "//*[@onclick]")
                for c in clickables:
                    try:
                        driver.execute_script("arguments[0].click();", c)
                    except:
                        pass

                time.sleep(2)  # wait for content to load after clicking

                # --- EXTRACT PDF LINKS FROM MAIN PAGE ---
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")

                pdf_links = set()

                for link in soup.find_all("a", href=True):
                    href = link["href"]
                    if href.lower().endswith("\r"):
                        href = href[:-1]
                    print('link is: ' + str(href))
                    print(href.lower().endswith(".pdf"))
                    if href.lower().endswith(".pdf"):
                        full = requests.compat.urljoin(pdf_file_url, href)
                        pdf_links.add(full)

                # --- CHECK IFRAMES AS WELL ---
                iframes = driver.find_elements(By.TAG_NAME, "iframe")
                for frame in iframes:
                    try:
                        driver.switch_to.frame(frame)
                        html = driver.page_source
                        soup = BeautifulSoup(html, "html.parser")

                        for link in soup.find_all("a", href=True):
                            href = link["href"]
                            if href.lower().endswith(".pdf"):
                                full = requests.compat.urljoin(pdf_file_url, href)
                                pdf_links.add(full)

                        driver.switch_to.default_content()
                    except:
                        pass

                driver.quit()

                print(f"Found {len(pdf_links)} PDFs:")
                for url in pdf_links:
                    print(url)

                # --- DOWNLOAD AND EXTRACT ---
                for pdf_url in pdf_links:
                    # Get filename from URL
                    filename = os.path.basename(urlparse(pdf_url).path)
                    if not filename.lower().endswith(".pdf"):
                        filename += ".pdf"

                    pdf_file = os.path.join(OUTPUT_FOLDER, filename)
                    print('pdf path is: ' + pdf_file)
                    md_file = os.path.join(OUTPUT_FOLDER, filename.replace(".pdf", ".md"))

                    try:
                        # Download pdf
                        print(f"Downloading {pdf_url}")
                        data = requests.get(pdf_url)
                        with open(pdf_file, "wb") as f:
                            f.write(data.content)

                        print('The path exists: ' + str(os.path.exists(pdf_file)))

                        # Extract text from pdf
                        pdf_to_markdown_with_github(pdf_file, API_KEY, REPO, BRANCH, TOKEN, md_file,
                                                    os.path.join('images', path.replace('.json', '')),
                                                    os.path.join('outputs', path.replace('.json', '')))


                    except Exception as e:
                        print(f"Error with {pdf_url}: {e}")

                print("✅ Done: PDFs downloaded and text extracted.")