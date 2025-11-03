# pip install selenium
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.bnr.ro/9100-cursul-de-schimb-serii-zilnice')
# print(driver)
time.sleep(1)
table_head = driver.find_element(by=By.XPATH, value='//*[@id="reper"]/div/div/table/thead')
table_body = driver.find_element(by=By.XPATH, value='//*[@id="reper"]/div/div/table/tbody')
# print(table_head.text)
# print(table_body.text)
header = table_head.text.split()
body = table_body.text.split()
# print(header)
# print(body)

skip = False
final_header = []
for i in range(len(header)):

    if skip:
        skip = False
        continue

    if header[i] == '100':
        final_header.append(header[i] + " " + header[i+1])
        skip = True
    else:
        final_header.append(header[i])

# print(final_header)
# print(len(final_header))


# TABEL GENERAT PE RANDURI

# body_rows = []
# for i in range(0, len(body), len(final_header)):
#     counter = i
#     body_rows.append(body[counter: counter + len(final_header)])
# print(body_rows)

# df = pd.DataFrame(body_rows, columns=final_header)
# print(df)
# df.to_excel("Tabel curs.xlsx", index=False)

# TABEL GENERAT PE COLOANE

# body_columns = []
# for i in range(len(final_header)):
#     body_columns.append({i: []})

body_columns = {i: [] for i in range(len(final_header))}
# print(body_columns)

# {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: [], 26: [], 27: [], 28: [], 29: [], 30: [], 31: [], 32: [], 33: [], 34: [], 35: [], 36: [], 37: [], 38: []}
# ['03.11.2025', '2,8921', '2,6005', '3,1449', '5,4698', '0,2090', '0,6811', '0,0934', '5,0861', '5,7988', '1,3141', '2,8648', '0,2580', '0,4365'

counter = 0
for j in body:
    body_columns[counter % len(final_header)].append(j)
    counter += 1
# print(body_columns)

df = pd.DataFrame(body_columns)
df.to_excel('Tabel curs_2.xlsx', header=final_header, index=False)