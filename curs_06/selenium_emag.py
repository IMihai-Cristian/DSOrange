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

    # if title and "pentru seniori" in title.lower():
    if title and "pink" in title.lower():
        # print(title, ' ----> ', price)
    # else:
    #     print(' ===================== ')
        price_comp = price.strip().replace('.', '').replace(',', '.').split(' ')[0]
        # print(price_comp, type(price_comp))
        if 4700 <= float(price_comp) <= 5000:
            # print(title, price)
            try:
                button = card.find_element(By.CSS_SELECTOR, "button.yeahIWantThisProduct")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                time.sleep(0.5)
                button.click()
                try:
                    wait = WebDriverWait(driver, 5)
                    go_to_cart = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-test='atc-modal-cart-details']")))
                    # go_to_cart = driver.find_element(By.CSS_SELECTOR, "a[data-test='atc-modal-cart-details']")
                    # driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", go_to_cart)
                    # print(go_to_cart, type(go_to_cart))
                    driver.execute_script("arguments[0].scrollIntoView(true);", go_to_cart)
                    # time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", go_to_cart)
                    # cart_url = go_to_cart.get_attribute('href')
                except:
                    print('Nu se observa butonul')
                    cart_url = "https://www.emag.ro/cart/products?ref=add-to-cart-module_go-to-cart_button"
                    driver.get(cart_url)
                    try:
                        continue_button = driver.find_element(By.CSS_SELECTOR, "a[href='/cart/checkout']")
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_button)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", continue_button)
                    except:
                        print('Nu am dat click pe Continue')
                        checkout = "https://www.emag.ro/cart/checkout"
                        driver.get(checkout)
                    wait = WebDriverWait(driver, 10)
                    email_input = wait.until(EC.visibility_of_element_located((By.ID, "user_login_email")))
                    email_input.send_keys('exemplu@email.com')
            except Exception as e:
                print(f"Nu am putut adauga in cos: {title}")
                print(e)

