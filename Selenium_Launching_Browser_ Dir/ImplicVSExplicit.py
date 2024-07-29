"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.chrome.service import service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.service import service, Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = 'C:\\Program Files\\Python312\\Scripts\\chromedriver.exe'

service = Service(chrome_path)
options = Options()
# driver = webdriver.chrome(service=service,options=options)
driver = webdriver.Chrome(service=service, options=options)
my_Explicit = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

driver.implicitly_wait(13)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
username_explicit_condition = my_Explicit.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
username_explicit_condition.send_keys("Admin")
time.sleep(4)
password_Explicit = my_Explicit.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
password_Explicit.send_keys("admin123")
driver.implicitly_wait(5)
time.sleep(7)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.quit()

# This the Implicit wait and Explicit wait ( It is very very important for testing to wait the webelements )
# To avoid synchroziation errors we use these waits
# Our Automation scripts as more control on Applications , We can sync our automation scripts vs application performs
# Our automation scripts we need to pause some times and in the application our webelements to be displayed
# ( we don't increase the application performance but we can pause our automation scripts for sometimes the elements to be displayed )
# Implicit wait  - will work on the time period
# Explicit wait - will work on the conditions ( We can control or Ignore  the exception in explicit wait )
