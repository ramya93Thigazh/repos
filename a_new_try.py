import time

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.order(1)
def test_goo_login(setup):
    driver=setup
    driver.get("https://www.google.co.in")
    s_box = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
    s_box.send_keys("amazon")
    s_box.submit()
    time.sleep(20)
    amazon_page = driver.find_element(By.XPATH,"//span[contains(text(),'Shop online at Amazon India')]")
    amazon_page.click()
    time.sleep(10)



@pytest.mark.order(2)
def test_a_page(setup):
    driver = setup
    driver.get("https://www.amazon.in/")
    time.sleep(10)
    a_search_box = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
    a_search_box.click()
    a_search_box.send_keys("iphone")
    a_search_box.submit()
    time.sleep(10)
    pink_iphone = driver.find_element(By.XPATH, "//a/span[1][contains(text(),'Apple iPhone 13 (128GB) - Pink')]")
    pink_iphone.click()
    time.sleep(10)
    price=driver.find_element(By.XPATH,"(//span[contains(@class,'a-price-whole')])[5]")
    price_txt=price.text
    print(price_txt)