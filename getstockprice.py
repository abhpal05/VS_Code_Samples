
import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/ITC.NS'

r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.title.text)