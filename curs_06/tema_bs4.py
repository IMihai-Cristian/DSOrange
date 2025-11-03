import requests
import pandas
from bs4 import BeautifulSoup

req = requests.get('https://www.exchangerates.org.uk/EUR-USD-exchange-rate-history.html')
print(req)
link = BeautifulSoup(req.text, features='html.parser')
# print(type(link))
# print(link)
