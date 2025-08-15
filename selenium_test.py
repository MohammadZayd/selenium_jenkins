from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# Set up Chrome options for Jenkins/Docker environment
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open a webpage
driver.get("https://aws.amazon.com/")
time.sleep(5)  # Wait for the page to load

# Make the browser full screen
driver.fullscreen_window()

# Take screenshot
screenshot_path = os.path.join(os.getcwd(), "aws_screenshot.png")
driver.save_screenshot(screenshot_path)

# Quit driver
driver.quit()

print(f"Screenshot saved to: {screenshot_path}")
