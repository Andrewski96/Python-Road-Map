import requests
from bs4 import BeautifulSoup
import csv

value = requests.get("https://www.cnn.com")
soup = BeautifulSoup(value.text, "html.parser")
secHeadings = soup.find_all("a")
for tag in secHeadings:
    print(tag.text)
    data = [
        {"title": "Headline 1", "link": "https://cnn.com/1"},
        {"title": "Headline 2", "link": "https://cnn.com/2"}
    ]
with open("cnn_headlines.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerow(data)