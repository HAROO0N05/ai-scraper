import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

data = []
for p in paragraphs:
    text = p.get_text(strip=True)
    if len(text) > 50:
        data.append({"content": text})

with open("scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Done! Scraped {len(data)} paragraphs.")