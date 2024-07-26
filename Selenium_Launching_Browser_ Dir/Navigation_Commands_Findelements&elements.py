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
driver.get("https://www.nopcommerce.com/en/demo")
driver.maximize_window()
footer_scroll = driver.find_element(By.XPATH, "//*[@class='footer-upper']")

# Scroll the "Footer" element into view
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView();", footer_scroll)
time.sleep(5)
driver.find_element(By.XPATH, "//a[text()='Store demo']").click()
time.sleep(8)
store_demo_text = driver.find_element(By.XPATH, "//h1[text()='nopCommerce Store Demo']")
store_demo_text.is_displayed()
print("Store demo text :: ", store_demo_text.text)
time.sleep(2)
# back to url home _ en
driver.get("https://www.nopcommerce.com/en")

time.sleep(10)
driver.refresh()
time.sleep(8)

# Capture the current url , if it is matched the current vs Actual url link
commerce_com = driver.current_url
print("Current_Url is :", commerce_com)

expected_url = "https://www.nopcommerce.com/en"

if commerce_com == expected_url:
    print("The current url Vs expected url is matched ::")
else:
    print("Current url Vs Expected_url is not matched ")
time.sleep(4)
footer_scroll = driver.find_element(By.XPATH, "//*[@class='footer-upper']")

# Scroll the "Footer" element into view
time.sleep(5)

our_clients_scroll = driver.find_element(By.XPATH, "//footer[@class='footer']")
driver.execute_script("arguments[0].scrollIntoView();", our_clients_scroll)
time.sleep(9)

# ****************************************************************************

print("**************** Find_element Vs Find_elements ")

# Test Scenario 1 : The single web element and  find element method  is matched and working fine ;
footer_all_Links_31 = driver.find_elements(By.XPATH, "//ul[@class='list']/child::li")
print("Print showcase text", footer_all_Links_31[2].text)  # Show case

for i in footer_all_Links_31:
    print("all 31 links text should be displayed ::", i.text)

time.sleep(4)
# driver.back()
# driver.refresh()

driver.quit()
"""
driver.get("https://www.flipkart.com/")

# Same browser window, We opened the two different web applications ;
# Back, forward,refresh commands
#  Back command
driver.back()  # It will navigate to the snapdeal.com

# move forward command
driver.forward()  # now it will navigate to the flipkart page

# refresh command
driver.refresh()  # the flipkart page is refresh

# Finally quite the browser window
driver.quit()
"""
