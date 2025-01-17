#how to handle more then one windows
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
service = Service(executable_path=ChromeDriverManager().install())


driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Alerts.html")
originalWindow = driver.current_window_handle
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.open('https://www.google.co.in')")
time.sleep(5)
driver.switch_to.window(originalWindow)
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
time.sleep(5)