import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_orange_website_navigation():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Open the Orange website
        driver.get("https://www.orange.com/en")

        # Handle cookies (assuming there's a button to accept cookies with id 'accept-cookies')
        accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "accept-cookies")))
        accept_cookies.click()

        # Click on Magazines
        magazines = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Magazines")))
        magazines.click()

        # Click on Orange Business
        orange_business = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Orange Business")))
        orange_business.click()
        # Validate the title of the new window
        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert "Orange Business" in driver.title

        # Go back to the previous window and close the browser
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main()