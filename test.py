import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.sc.com/in/")
time.sleep((10))
login=driver.find_element(By.XPATH,"//button[contains(@title,'Login')]")
login.click()
time.sleep(10)
onlinebank=driver.find_element(By.CSS_SELECTOR,"a[title='Online Banking Login']")
onlinebank.click()

wait=WebDriverWait(driver,100)
contologin=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[title='Continue to Login']")))
contologin.click()
time.sleep(10)
acttit=driver.title
print("title",acttit)
expectedtitle="Standard Chartered India"
if acttit.__contains__(expectedtitle):
    print("YOU ARE IN LOGIN PAGE")
else:
    print("WRONG WINDOW")
