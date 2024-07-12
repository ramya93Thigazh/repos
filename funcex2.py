from pomex2 import search_page
import time

def sear(driver):
    s=search_page(driver)
    s.search("amazon")
    s.find_Lpage()
    time.sleep(10)
