
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

# Path to the Chrome WebDriver executable
chrome_driver_path = 'C:\\Program Files\\Python312\\Scripts\\chromedriver.exe'

# Create a Service object
service = Service(chrome_driver_path)

# Create Options object
options = Options()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize the browser window
driver.maximize_window()

# Wait for a few seconds to observe the browser state
time.sleep(5)  # Wait for 5 seconds

act_title = driver.title  # alt +shift + Enter
expected_title = "OrangeHRM"

if act_title == expected_title:
    print(" The title is matched with act and  expected title")
else:
    print("The expected and actual title is not matched")
time.sleep(4)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)
driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

# Path to the Chrome WebDriver executable
chrome_driver_path = 'C:\\Program Files\\Python312\\Scripts\\chromedriver.exe'

# Create a Service object
service = Service(chrome_driver_path)

# Create Options object
options = Options()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # //a[text()='OrangeHRM, Inc']

# Maximize the browser window
driver.maximize_window()

driver.find_element(By.XPATH, "//p[text()='Forgot your password? ']").click()
driver.find_element(By.XPATH, "//a[text()='OrangeHRM, Inc']").click()
time.sleep(4)
driver.close()

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

    # Wait for the "Forgot your password?" link to be clickable and then click it
    forgot_password_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Forgot your password? ']"))
    )
    forgot_password_element.click()

    # Wait for the "OrangeHRM, Inc" link to be clickable and then click it
    orangehrm_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='OrangeHRM, Inc']"))
    )
    orangehrm_link.click()

    # Wait for a few seconds to observe the result
    time.sleep(4)

finally:
    # Close the browser
    driver.quit()
