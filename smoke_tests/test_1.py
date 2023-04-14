import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'
driver = webdriver.Chrome()


def login(url, driver):
    driver.get(url=url)

    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')

    username.send_keys('standard_user')
    password.send_keys('secret_sauce')

    password.send_keys(Keys.ENTER)

    time.sleep(3)


def test_1(url, driver):
    login(url, driver)

    """[INFO] Product_Backpack """
    product_name = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text

    add_to_cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart.click()
    time.sleep(2)

    cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    cart.click()
    time.sleep(2)

    """[INFO] Product_Backpack IN CART """

    product_name_cart = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    product_price_cart = driver.find_element(By.XPATH,
                                             '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text

    assert product_name == product_name_cart
    assert product_price == product_price_cart

    checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout_button.click()

    """[INFO] CHECKOUT FORM """
    first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

    first_name.send_keys('Alex')
    last_name.send_keys('Pronto')
    zip_code.send_keys(11234)

    time.sleep(2)

    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()

    time.sleep(2)

    """[INFO] CHECKOUT: FINISH PAGE"""
    product_name_finish = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    product_price_finish = driver.find_element(By.XPATH,
                                               '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text

    assert product_name_cart == product_name_finish
    assert product_price_cart == product_price_finish

    finish_order = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish_order.click()

    print('Test Success')


def main():
    test_1(URL, driver)


if __name__ == '__main__':
    main()
