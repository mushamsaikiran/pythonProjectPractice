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

time.sleep(5)
#driver.find_element(By.XPATH("//*[text()='OrangeHRM, Inc']")).click()
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
driver.close()

