import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.alert import Alert

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.order(1)
def test_getpage(setup):
    driver=setup
    driver.get("https://demo.automationtesting.in/Alerts.html")
    title=driver.title
    print(f"TITLE OF THE CURRENT PAGE IS {title}")
    time.sleep(10)
    button=driver.find_element(By.XPATH,"//button[@class='btn btn-danger']")
    button.click()
    alert=Alert(driver)
    alert.accept()
    time.sleep(10)
    Falert=driver.find_element(By.XPATH,"(//a[@class='analystic'])[2]")
    Falert.click()
    clickbut=driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
    clickbut.click()
    driver.switch_to.alert.dismiss()



    """Getcookies=driver.get_cookies()
    for cookie in Getcookies:
        print(f"cookie in getcookie is{cookie}")
    time.sleep(10)
    addcookie={'name':'ramya','value':'42354676'}
    driver.add_cookie(addcookie)
    afteradd=driver.get_cookies()
    for cookie in afteradd:
        print(f"cookies in after adding{cookie}")
    Getcookie=driver.get_cookie('ramya')
    print(Getcookie)
    time.sleep(10)
    driver.delete_cookie('42354676')
    print("ramya cookie is sucessfully deleted")"""


"""@pytest.mark.order(2)
def test_login(setup):
    driver=setup
    driver.get("https://www.facebook.com")
    wait=WebDriverWait(driver,500)
    wait.until(EC.visibility_of(driver.find_element(By.ID,"reg_pages_msg")))
    time.sleep(10)
    Etbox=driver.find_element(By.ID,"email")
    Etbox.send_keys("ramyamam93@gmail.com")
    time.sleep(10)
    Ptbox=driver.find_element(By.ID,"pass")
    Ptbox.send_keys("ramya93@Mam")
    time.sleep(5)
    loginbotton=driver.find_element(By.NAME,"login")
    loginbotton.submit()
    Orig=driver.current_window_handle
    print(Orig)
    time.sleep(10)
    driver.execute_script("window.open('https://www.google.co.in')")
    driver.switch_to.window(driver.window_handles[1])
    Title = driver.title
    print(Title)
    driver.get("https://demo.automationtesting.in")
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.forward()
    time.sleep(10)
    driver.refresh()"""








