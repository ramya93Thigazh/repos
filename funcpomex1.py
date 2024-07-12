import time

from classpomex1 import login_page


def login(driver):
    log = login_page(driver)
    log.enter_username(UserText="user")
    log.enter_password(PassText="pass")
    log.login()
    time.sleep(10)
