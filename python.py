from scraper import scrape
from database import view_jobs

scrape()

data = view_jobs()

for row in data:
    print(row)
