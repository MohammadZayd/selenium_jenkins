from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")  # Set viewport size

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open a webpage
driver.get("http://docs.brhsoft.com/documents")
driver.implicitly_wait(10)

input_name = driver.find_element(By.XPATH, value="//input[@formcontrolname='userName']")
input_name.send_keys("admin@example.com")

input_password = driver.find_element(By.XPATH, value="//input[@formcontrolname='password']")
input_password.send_keys("12345678")

submit_button = driver.find_element(By.XPATH, value="//button[@type='submit']")
submit_button.click()
time.sleep(5)  # Wait for the page to load

# Take screenshot
screenshot_path = os.path.join(os.getcwd(), "aws_screenshot.png")
driver.save_screenshot(screenshot_path)

# Quit driver
driver.quit()

print(f"Screenshot saved to: {screenshot_path}")
