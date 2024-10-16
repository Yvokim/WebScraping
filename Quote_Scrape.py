import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'

response = requests.get(url)

if response.status_code == 200:
    # Parse html content
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f'Quote: {text}\nAuthor:{author}\n')

    else:
        print(f'Failed to retrieve quotes.Status code:{response.status_code}')
