from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    wait = WebDriverWait(driver, 10)

    # Fill the form using explicit waits
    first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
    first_name.send_keys("John")

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("Doe")

    gender = driver.find_element(By.ID, "sex-0")  # Male radio button
    gender.click()

    experience = driver.find_element(By.ID, "exp-2")  # 3 years
    experience.click()

    # Date
    driver.find_element(By.ID, "datepicker").send_keys("12/31/2025")

    # Profession
    driver.find_element(By.ID, "profession-1").click()  # Automation Tester

    # Tools
    driver.find_element(By.ID, "tool-2").click()  # Selenium Webdriver

    # Submit button
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()

    print("Form submitted successfully!")

    driver.quit()

if __name__ == "__main__":
    test_form_submission()
