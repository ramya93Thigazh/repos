import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("mailid,password",[("ramya93@gmail.com","ramya@93"),("suresh@91gmail.com","suresh@91"),("thigazh18@gmail.com","thigazh@18"),])
def test_login(driver,mailid,password):
    driver.get("https://www.facebook.com/login/")
    m_id=driver.find_element(By.XPATH,"//input[contains(@id,'email')]")
    m_id.send_keys(mailid)
    m_id.submit()
    time.sleep(10)
    pas=driver.find_element(By.XPATH,"//input[@id='pass']")
    pas.send_keys(password)
    pas.submit()
    print("your login mail id is {}and password is {}".format(mailid,password))



