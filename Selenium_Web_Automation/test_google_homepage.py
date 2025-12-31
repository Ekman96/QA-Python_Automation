from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_homepage():
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed(), "Search box not found"

    driver.quit()
