from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#https://www.google.co.in/

class search_page:
    def __init__(self,driver):
        self.driver=driver
        self.serloc=(By.ID,"APjFqb")
        self.loginloc=(By.XPATH,"(//a/h3[@class='LC20lb MBeuO DKV0Md'])[1]")
    def search(self,searchtext):
        searchbox=WebDriverWait(self.driver,100).until(EC.presence_of_element_located(self.serloc))
        searchbox.send_keys(searchtext)
        searchbox.submit()
    def find_Lpage(self):
        findpage=WebDriverWait(self.driver,100).until(EC.presence_of_element_located(self.loginloc))
        findpage.click()

