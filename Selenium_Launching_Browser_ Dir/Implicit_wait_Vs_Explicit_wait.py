import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Path to the Chrome WebDriver executable
chrome_driver_path = 'C:\\Program Files\\Python312\\Scripts\\chromedriver.exe'

# Create a Service object
service = Service(chrome_driver_path)

# Create Options object
options = Options()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)
# driver.implicitly_wait(12)
my_wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(9)

Username_Input = driver.find_element(By.XPATH, "//input[@name='username']")
Username_Input.send_keys("Admin")

Password_Input = driver.find_element(By.XPATH, "//input[@name='password']")
Password_Input.send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(6)

# driver.implicitly_wait(10)
assign_leave = my_wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Assign Leave']")))
assign_leave.click()
# driver.find_element(By.XPATH, "//button[@title='Assign Leave']").click()
text_input_filed = my_wait.until(EC.presence_of_element_located((By.XPATH,
                                                                 "(//input[@placeholder='Type for hints...'])[1]")))
text_input_filed.send_keys("sai")
time.sleep(9)
driver.quit()
