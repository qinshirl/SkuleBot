# utils/cache_ece_courses.py
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

CALENDAR_URL = "https://engineering.calendar.utoronto.ca/undergraduate-program-electrical-engineering-aeelebasc"
BASE_URL = "https://engineering.calendar.utoronto.ca"


def get_rendered_html(url: str) -> str:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1)  # Wait for JS to load
    html = driver.page_source
    driver.quit()
    return html


def scrape_and_cache_courses(output_path="utils/ece_courses.json"):
    print("[INFO] Fetching main calendar page...")
    html = get_rendered_html(CALENDAR_URL)
    soup = BeautifulSoup(html, "html.parser")

    course_links = soup.select("a[href^='/course/ECE']")
    print(f"[INFO] Found {len(course_links)} ECE courses")

    courses = []
    for link in course_links:
        code = link.text.strip()
        title_tag = link.find_next(string=True)
        title = title_tag.strip(" :\"\n") if title_tag else ""
        url = BASE_URL + link["href"]

        print(f"[INFO] Fetching description for {code}...")
        course_html = get_rendered_html(url)
        course_soup = BeautifulSoup(course_html, "html.parser")

        desc_wrapper = course_soup.find("div", class_="field field--name-field-desc")
        desc_div = desc_wrapper.find("div", class_="w3-bar-item field__item") if desc_wrapper else None
        description = desc_div.get_text(strip=True) if desc_div else "Description not found."

        courses.append({
            "code": code,
            "title": title,
            "url": url,
            "description": description
        })

    with open(output_path, "w") as f:
        json.dump(courses, f, indent=2)

    print(f"[SUCCESS] Cached {len(courses)} courses to {output_path}")


if __name__ == "__main__":
    scrape_and_cache_courses()
