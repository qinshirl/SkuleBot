import base64
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from pdfminer.high_level import extract_text
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import fitz
import io
import os
import time
import json


def read_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    return data


def ocr_pdf(pdf_path):
    text = ""
    # Convert each page to an image
    images = convert_from_path(pdf_path, dpi=300)

    for i, img in enumerate(images):
        print(f"    OCR page {i + 1}/{len(images)}")
        text += pytesseract.image_to_string(img)

    return text


if __name__ == '__main__':
    json_file_list = ['Electrical and Computer Engineering.json']
    for path in json_file_list:
        data_dict = read_json(path)
        for key in data_dict:
            OUTPUT_FOLDER = path.replace('.json', '') + ' ---- ' + key
            os.makedirs(OUTPUT_FOLDER, exist_ok=True)
            for pdf_file_url in data_dict[key]:
                # 1. Launch Selenium browser
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
                    txt_file = os.path.join(OUTPUT_FOLDER, filename.replace(".pdf", ".txt"))

                    try:
                        # Download pdf
                        print(f"Downloading {pdf_url}")
                        data = requests.get(pdf_url)
                        with open(pdf_file, "wb") as f:
                            f.write(data.content)

                        # Extract text from pdf
                        text = extract_text(pdf_file)
                        print('Type of text is: ' + str(type(text)))
                        print('Length of text is: ' + str(len(text.strip())))
                        # Use OCR to extract text from images in pdf if the pdf contains only images
                        if len(text.strip()) < 50:
                            print("PDF has no text — using OCR...")
                            text = ocr_pdf(pdf_file)

                        with open(txt_file, "w", encoding="utf-8") as f:
                            f.write(text)

                    except Exception as e:
                        print(f"Error with {pdf_url}: {e}")

                print("✅ Done: PDFs downloaded and text extracted.")