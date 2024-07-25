import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def setup():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.order(1)
def test_goo_login(setup):
    driver = setup
    driver.get("https://www.google.co.in")
    s_box=driver.find_element(By.XPATH,"//textarea[@class='gLFyf']")
    s_box.send_keys("amazon")
    amazon_page = driver.find_element(By.XPATH, "(//h3[@class='LC20lb MBeuO DKV0Md'])[1]")
    amazon_page.click()
    a_search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    a_search_box.send_keys("iphone")
    pink_iphone = driver.find_element(By.XPATH, "//span[contains(text(),'Apple iPhone 13 (128GB) - Pink')]")
    pink_iphone.click()


@pytest.mark.order(2)
def test_a_page(setup):
    driver = setup
    driver.get("https://www.amazon.in/")
    amazon_page=driver.find_element(By.XPATH,"(//h3[@class='LC20lb MBeuO DKV0Md'])[1]")
    amazon_page.click()
    a_search_box=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
    a_search_box.send_keys("iphone")
    pink_iphone=driver.find_element(By.XPATH,"//span[contains(text(),'Apple iPhone 13 (128GB) - Pink')]")
    pink_iphone.click()




