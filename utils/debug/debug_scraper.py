import requests
from bs4 import BeautifulSoup

url = "https://engineering.calendar.utoronto.ca/course/aps110h1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Send the GET request with browser headers
response = requests.get(url, headers=headers)

# Show raw HTML length (to verify we're not blocked or redirected)
print(f"[DEBUG] Page length: {len(response.text)}")

# Parse the response with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Try extracting the course description
# desc_wrapper = soup.find("div", class_="field field--name-field-desc")
desc_wrapper = soup.find("div", class_="field--name-field-desc")

if desc_wrapper:
    desc_div = desc_wrapper.find("div", class_="field__item")
    if desc_div:
        print("[FOUND] Description:")
        print(desc_div.get_text(strip=True))
    else:
        print("[DEBUG] field__item not found inside description wrapper.")
else:
    print("[DEBUG] field--name-field-desc not found.")

# if desc_wrapper:
#     desc_div = desc_wrapper.find("div", class_="w3-bar-item field__item")
#     if desc_div:
#         print("[FOUND] Description:")
#         print(desc_div.get_text(strip=True))
#     else:
#         print("[DEBUG] field__item not found in field--name-field-desc")
# else:
#     print("[DEBUG] field--name-field-desc not found in HTML")

# Optional: print the start of raw HTML for visual inspection
print("\n--- START OF RAW HTML ---")
# print(response.text[:500])  # print only first 500 chars
# with open("debug_page_dump.html", "w") as f:
#     f.write(response.text)
# print("[DEBUG] Dumped HTML to debug_page_dump.html")



