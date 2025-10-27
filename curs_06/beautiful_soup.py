import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bnr.ro/9100-cursul-de-schimb-serii-zilnice')
# print(req)
link = BeautifulSoup(req.text, features='html.parser')
# print(type(link))
# print(link)

main = link.find_all('div', attrs={'id': 'wrapper'})
# main = link.find_all('table')
print(main)