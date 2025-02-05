import time
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from conftest import driver
from locators.login_locator import *

url = "https://the-internet.herokuapp.com/"


@pytest.mark.skip
def test_google(driver):
    driver.get(url)
    assert driver.current_url.__eq__(url)


def test2(driver):
    title = "The Internet"
    start_time = time.time()
    locator = (By.CSS_SELECTOR, "a[href='/abtest']")
    locator2 = (By.XPATH, "//a[text()='A/B Testing']")
    driver.get(url)
    driver.find_element(*locator).click()
    print(time.time() - start_time)
    assert driver.current_url == "https://the-internet.herokuapp.com/abtest"
    driver.back()
    assert driver.current_url == "https://the-internet.herokuapp.com/"
    driver.refresh()
    assert driver.current_url == "https://the-internet.herokuapp.com/"
    assert driver.title == title
    current_tab = driver.window_handles
    print(current_tab)
    driver.quit()


def test_login(driver):
    username = "standard_user"
    password = "secret_sauce"
    driver.get(url2)
    driver.find_element(By.CSS_SELECTOR, username_field).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, password_field).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, login_button).click()
    sleep(1)
    assert driver.find_element(By.XPATH, app_logo).is_enabled()
    sleep(1)
    assert driver.current_url == home_page


def test_letcode(driver):
    url3 = "https://letcode.in/selectable"
    list_item_locator = "(//div[@id='selectable'])[4]"
    postman_element = "//*[contains(@class,'ui-selected')]/h3[text()='TestNg']"
    driver.get(url3)
    sleep(1)
    driver.find_element(By.XPATH, list_item_locator).click()
    assert driver.find_element(By.XPATH, postman_element).is_displayed()
    sleep(1)
