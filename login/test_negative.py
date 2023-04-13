import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'
driver = webdriver.Chrome()


def login(url, driver):
    driver.get(url=url)

    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')

    username.send_keys('error data')
    password.send_keys('error data')

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()

    time.sleep(3)


def test_1(url, driver):
    login(url, driver)

    warning_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert warning_text.text == 'Epic sadface: Username and password do not match any user in this service'
    print('negative login test success')


def main():
    test_1(URL, driver)


if __name__ == '__main__':
    main()
