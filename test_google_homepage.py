from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Simple UI test: open Google, search, and check the title
def test_google_homepage():
    # Start the browser (Chrome)
    driver = webdriver.Chrome()  # Selenium Manager will download the driver automatically

    try:
        # Open Google
        driver.get("https://www.google.com")
        driver.maximize_window()

        # Wait a bit so we can see it
        time.sleep(2)

        # Check page title contains "Google"
        if "Google" in driver.title:
            print("[PASS] Google homepage loaded successfully.")
        else:
            print("[FAIL] Google homepage title was:", driver.title)

    finally:
        # Close the browser
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_google_homepage()
