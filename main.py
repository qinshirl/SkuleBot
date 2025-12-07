import base64
import os
import fitz
import requests
import time
import json
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


# -------------------------------
# 2) Split PDF into single-page PDFs under 1MB
# -------------------------------
def split_pdf_into_pages_under_limit(input_pdf, output_dir='split_pages', max_kb=1024):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(input_pdf)
    page_pdfs = []

    for i in range(doc.page_count):
        out_path = os.path.join(output_dir, f"page_{i+1:03}.pdf")
        single = fitz.open()
        single.insert_pdf(doc, from_page=i, to_page=i)
        single.save(out_path)
        single.close()

        # compress if needed
        for _ in range(3):
            if os.path.getsize(out_path) <= max_kb*1024:
                break
            tmp = out_path.replace(".pdf", "_cmp.pdf")
            tmp_doc = fitz.open(out_path)
            tmp_doc.save(tmp, deflate=True, garbage=4)
            tmp_doc.close()
            if os.path.getsize(tmp) < os.path.getsize(out_path):
                os.remove(out_path)
                os.rename(tmp, out_path)
            else:
                os.remove(tmp)
                break

        page_pdfs.append(out_path)

    doc.close()
    return page_pdfs

# -------------------------------
# 3) OCR via OCR.space API
# -------------------------------
def ocr_space_image(image_path, api_key):
    url = "https://api.ocr.space/parse/image"
    with open(image_path, "rb") as f:
        r = requests.post(url,
                          files={"file": f},
                          data={"apikey": api_key, "language": "eng"})
    try:
        return r.json()["ParsedResults"][0]["ParsedText"]
    except:
        return "*No text found*"

def extract_text_from_single_page_pdf(page_pdf_path, api_key):
    doc = fitz.open(page_pdf_path)
    page = doc.load_page(0)
    text = page.get_text("text").strip()
    doc.close()
    if text and len(text.split()) > 3:
        return text
    # fallback to OCR
    from PIL import Image
    import io

    # render page as image in memory
    doc = fitz.open(page_pdf_path)
    pix = doc.load_page(0).get_pixmap()
    img_bytes = pix.tobytes("png")
    doc.close()

    # save temporarily
    tmp_img = page_pdf_path.replace(".pdf", "_ocr.png")
    with open(tmp_img, "wb") as f:
        f.write(img_bytes)

    ocr_text = ocr_space_image(tmp_img, api_key)
    os.remove(tmp_img)
    return ocr_text or "*No text found*"

# -------------------------------
# 4) Full pipeline: PDF → Text → Markdown → GitHub
# -------------------------------
def pdf_to_markdown_with_github_text_only(input_pdf, api_key, repo, branch, token,
                                          output_md, outputs_remote_folder):
    # 1) Split PDF
    page_pdfs = split_pdf_into_pages_under_limit(input_pdf)
    md_blocks = []

    for idx, page_pdf in enumerate(page_pdfs, start=1):
        print(f"Processing page {idx}/{len(page_pdfs)} -> {page_pdf}")

        # 2) Extract text
        text = extract_text_from_single_page_pdf(page_pdf, api_key)
        md_block = f"## Page {idx}\n\n{text}\n\n"
        md_blocks.append(md_block)

        # 3) Cleanup local page
        try: os.remove(page_pdf)
        except: pass

    # 4) Write Markdown locally
    full_md = "\n".join(md_blocks)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"Local Markdown saved: {output_md}")

    # 5) Upload Markdown to GitHub
    remote_md_path = f"{outputs_remote_folder}/{os.path.basename(output_md)}"
    md_url = github_upload(repo, branch, token, output_md, remote_md_path)
    print("Markdown uploaded:", md_url)

    return {"local_md": output_md, "remote_md_url": md_url}



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
                        pdf_to_markdown_with_github_text_only(pdf_file, API_KEY, REPO, BRANCH, TOKEN, md_file,
                                                    os.path.join('outputs', path.replace('.json', '_files')))


                    except Exception as e:
                        print(f"Error with {pdf_url}: {e}")

                print("✅ Done: PDFs downloaded and text extracted.")