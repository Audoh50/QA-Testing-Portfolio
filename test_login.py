from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Open Chrome browser
driver = webdriver.Chrome()

# Open sample login website
driver.get("https://the-internet.herokuapp.com/login")

# Maximize browser window
driver.maximize_window()

# Find username field and enter username
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# Find password field and enter password
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# Click the Login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Wait for page to load
time.sleep(2)

# Verify successful login
success_message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in success_message:
    print("TEST PASSED: User logged in successfully.")
else:
    print("TEST FAILED: Login was unsuccessful.")

# Close browser
driver.quit()
