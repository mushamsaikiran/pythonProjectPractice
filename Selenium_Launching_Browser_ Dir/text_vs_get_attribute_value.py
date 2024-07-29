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

    # Wait for the username input field to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )

    # Enter the username
    username_field.send_keys("Admin")
    print("Entered username")
    print("No inner text returned ", username_field.text)  #

    # Now you the get_attribute :
    print("get attribute value of name ", username_field.get_attribute("name"))
    print("get attribute value of placeholder in the input tag", username_field.get_attribute("placeholder"))
    login_get = driver.find_element(By.XPATH, "//button[@type='submit']")
    print(login_get.text)
finally:
    driver.quit()
