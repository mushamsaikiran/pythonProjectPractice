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

# Find element method :
# To import by class , Alt + shift + Enter
# absolute x path for the username : # Absolute x path will start from the root node
driver.find_element(By.XPATH,
                    "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
    "Admin")

# The relative x path for the password
driver.find_element(By.XPATH,
                    "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
    'admin@123')

driver.find_element(By.XPATH, "//*[@placeholder ='Username']").send_keys("Admin")

# absolute xpath or full x path for the password below :
driver.find_element(By.XPATH,
                    "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
    "admin123")
# Relative x path or partial x path for the password below :
driver.find_element(
    (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")).send_keys("admin123")

# manually written  x path for the password :

driver.find_element(By.XPATH, "//*[@placeholder ='Password']").send_keys("admin123")

driver.find_element(By.XPATH, "//*[@type ='submit']").click()
time.sleep(5)  # wait for 5 sec
# Close the browser
driver.close()

# In future use this code for the launch the browser and open browser and import the packages etc :
# ALT + Shift + Enter --> To import the packages from the webdriver ( auto import the packages from the short cut )
# cltr + alt + l --> for refactor the code etc


##  **************8  Locators practice 8 locators and function of locators ;
# Class name
driver.find_element(By.CLASS_NAME, 'oxd-input oxd-input--active')

# Id name :
driver.find_element(By.ID, "//*[text()='Login']").send_keys("Testing")
# name and classname
driver.find_element(By.NAME, 'username').send_keys("username")
# In the locators there are 8 locators
# 1. Id , 2, Class name ,name,Tagname, partial text , linktext,css selectors and x path

# Tag name
driver.find_element(By.TAG_NAME, '//a')

# Partial link locators
driver.find_element(By.PARTIAL_LINK_TEXT, '')


# Watch video again and practice it and what is the difference between partial link, link text and tag name
# Practice linktext, partial link text , and tagname again and watch video and practice it ,


#  X path in functions : or ,and ,contains and text and start-with functions

# Or X path function ;

