import requests
import pandas
from bs4 import BeautifulSoup

# req = requests.get('https://www.exchangerates.org.uk/EUR-USD-exchange-rate-history.html')
# # print(req)
# link = BeautifulSoup(req.text, features='html.parser')
# # print(type(link))
# # print(link)
#
# main = link.find_all('div', attrs={'id': 'hd-maintable'})
# # # main = link.find_all('table')
# # print(main)
# header_list = []
# dataset = []
# for elem in main[0].find_all('tr'):
#     # print(elem)
#     td_elem_list = []
#     if elem.find_all('th'):
#         for th_elem in elem.find_all('th'):
#             header_list.append(th_elem.get_text())
#     elif elem.find_all('td'):
#         for td_elem in elem.find_all('td'):
#             td_elem_list.append(td_elem.get_text())
#     if td_elem_list:
#         dataset.append(td_elem_list)
# # print(header_list)
# dataset.pop(0)
# dataset.pop(-1)
# # print(dataset)
#
# df = pandas.DataFrame(dataset, columns=header_list)
# # print(df)
# df.to_excel('Exchange_rate.xlsx', header=header_list, index=False)

# _____________________________________________________________________________________________________


# req = requests.get('https://www.exchangerates.org.uk/currency-symbols.html')
# link = BeautifulSoup(req.text, features='html.parser')
# main = link.find_all('div', attrs={'id': 'content'})
# print(main)

# header_list = []
# dataset = []
# for elem in main[0].find_all('tr'):
#     td_elem_list = []
#     element_td = elem.find_all('td')
#     if element_td:
#         for td_elem in element_td:
#             td_elem_list.append(td_elem.get_text())
#     if td_elem_list and len(td_elem_list) > 1:
#         dataset.append(td_elem_list)
# # print(dataset)
#
# final_dataset = []
# for item in dataset:
#     row = []
#     for value in item:
#         # print(value)
#         if value == 'Ph':
#             value = value.replace('Ph', 'Ph')
#         elif value == 'le':
#             value = value.replace('le', 'lei')
#         if value:
#             row.append(value)
#     final_dataset.append(row)
#
# # print(final_dataset)
# header = final_dataset.pop(0)
#
#
# df = pandas.DataFrame(final_dataset, columns=header)
# print(df)
# df.to_excel('Currency.xlsx', index=False)


# _____________________________________________________________________________________________________

req = requests.get('https://www.emag.ro/laptopuri/c?tree_ref=2172&ref=cat_tree_91')
link = BeautifulSoup(req.text, features='html.parser')
main = link.find_all('div', attrs={'class': 'card-v2'})
# print(main)
dataset = []
for elem in main:
    item_list = []
    title = elem.find('a', attrs={'class': 'card-v2-title fw-semibold mb-1 js-product-url'})
    # print(title)
    if title:
        product_title = title.text
        item_list.append(product_title)
        price = elem.find('p', attrs={'class': 'product-new-price'})
        if price:
            product_price = price.text
        else:
            product_price = ""
        item_list.append(product_price)
    if item_list:
        dataset.append(item_list)

# print(dataset)
df = pandas.DataFrame(dataset)
# print(df)
df.to_csv('Preturi Laptop.csv', sep=',')

