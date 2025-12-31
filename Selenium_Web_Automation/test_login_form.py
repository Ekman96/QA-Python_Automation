from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_form():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
    driver.get("https://opensource-demo.orangehrmlive.com/")  # Free test site

    # Fill login form
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Verify login success (check for dashboard)
    dashboard = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    assert dashboard.is_displayed(), "Login failed"

    driver.quit()

if __name__ == "__main__":
    test_login_form()
