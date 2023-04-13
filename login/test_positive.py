import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'
driver = webdriver.Chrome()


def login(url, driver):
    driver.get(url=url)

    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')

    username.send_keys('standard_user')
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()

    time.sleep(3)


def test_1(url, driver):
    login(url, driver)

    products = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert products.text == 'Products'


def main():
    test_1(URL, driver)


if __name__ == '__main__':
    main()
