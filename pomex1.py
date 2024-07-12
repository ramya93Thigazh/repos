from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from funcpomex1 import login


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://facebook.com")
login(driver)
#setup driver