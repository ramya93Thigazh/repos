from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from funcex2 import sear

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.co.in/")
sear(driver)
title=driver.title
print(f"page title is{title}")