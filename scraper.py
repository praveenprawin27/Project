import requests
from bs4 import BeautifulSoup
from database import insert_job

def scrape():
    url = "https://books.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("h3")

    for book in books:
        title = book.text.strip()
        insert_job(title, "Book Store")

    print("Data scraped and saved!")
