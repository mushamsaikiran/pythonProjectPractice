import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the Chrome WebDriver executable
chrome_driver_path = 'C:\\Program Files\\Python312\\Scripts\\chromedriver.exe'

# Create a Service object
service = Service(chrome_driver_path)

# Create Options object
options = Options()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Maximize the browser window
    driver.maximize_window()

    # Wait for the "Forgot your password?" link to be visible and clickable
    forgot_password_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Forgot your password? ']"))
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Forgot your password? ']"))
    )

    # Scroll to the "Forgot your password?" link
    driver.execute_script("arguments[0].scrollIntoView();", forgot_password_element)

    # Click the "Forgot your password?" link
    forgot_password_element.click()
    print("Clicked on 'Forgot your password?' link")

    # Wait for the "OrangeHRM, Inc" link to be visible and clickable
    orangehrm_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='OrangeHRM, Inc']"))
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='OrangeHRM, Inc']"))
    )

    # Scroll to the "OrangeHRM, Inc" link
    driver.execute_script("arguments[0].scrollIntoView();", orangehrm_link)

    # Click the "OrangeHRM, Inc" link
    orangehrm_link.click()
    print("Clicked on 'OrangeHRM, Inc' link")

    # Wait for a few seconds to observe the result
    time.sleep(4)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
