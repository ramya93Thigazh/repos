from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login_page:

    def __init__(self, driver):
        self.driver = driver
        self.usernameloc =(By.ID, "email")
        self.passwordloc = (By.ID, "pass")
        self.logloc = (By.NAME, "login")

    def enter_username(self, UserText):
        username = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.usernameloc))
        username.send_keys(UserText)

    def enter_password(self, PassText):
        password = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.passwordloc))
        password.send_keys(PassText)

    def login(self):
        log = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.logloc))
        log.click()
