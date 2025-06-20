import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "http://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    with open('quotes.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author'])  

        for quote in quotes:
            quote_text = quote.find('span', class_='text').text.strip()
            author = quote.find('small', class_='author').text.strip()
            writer.writerow([quote_text, author])

    print("✅ Quotes successfully saved to 'quotes.csv' with proper encoding.")
else:
    print("❌ Failed to retrieve the website. Status code:", response.status_code)
