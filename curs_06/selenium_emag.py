import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.emag.ro/')
element = driver.find_element(by=By.ID, value='searchboxTrigger')
element.send_keys('iphone 16')
element.submit()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#card_grid .card-v2')))

cards = driver.find_elements(By.CSS_SELECTOR, '#card_grid .card-v2')
# print(len(count_phones))
# print(len(cards))
for card in cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "a.card-v2-title").text
    except:
        title = 'Nu exista'
    try:
        price = card.find_element(By.CSS_SELECTOR, "p.product-new-price").text
    except:
        price = 'Fara Pret'

    if title and "pentru seniori" in title.lower():
        print(title, price)
    else:
        print(' ===================== ')