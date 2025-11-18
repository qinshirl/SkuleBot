import requests
from markdownify import markdownify as md

# 1. Website URL
url = "https://engineering.calendar.utoronto.ca/section/Electrical-and-Computer-Engineering"

# 2. Download HTML
response = requests.get(url)
html = response.text

# 3. Convert HTML to Markdown
markdown_text = md(html, heading_style="ATX")

# 4. Save to .md file
output_file = "output.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown_text)

print(f"Markdown saved to {output_file}")