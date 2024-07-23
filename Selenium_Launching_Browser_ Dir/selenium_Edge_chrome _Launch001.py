"""
# How to launch the browser in edge browser ;
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# Path to the Edge WebDriver executable
edge_driver_path = 'C:\Program Files\Python312\Scripts\msedgedriver.exe'

# Create a Service object
service = Service(edge_driver_path)

# Create Options object
options = Options()

# Initialize the Edge WebDriver
driver = webdriver.Edge(service=service, options=options)

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



# ************ How to open the chrome class driver but it closing very fast and not maximize the window   *****************

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to the Chrome WebDriver executable
chrome_driver_path = 'C:\Program Files\Python312\Scripts\chromedriver.exe'

# Create a Service object
service = Service(chrome_driver_path)

# Create Options object
options = Options()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize the  browser window
driver.maximize_window()

# Close the chrome driver
#driver.close()
"""

# The Browser launch successfully and maximize the window and close the window (Try this script if you wnat launch the browser )

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

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

# Close the browser
driver.close()

# In future use this code for the launch the browser and open browser and import the packages etc :
# ALT + Shift + Enter --> To import the packages from the webdriver ( auto import the packages from the short cut )
# cltr + alt + l --> for refactor the code etc
