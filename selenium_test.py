from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
driver.get("https://www.amazon.sa")
time.sleep(5)  # Wait for the page to load

# Take screenshot
screenshot_path = os.path.join(os.getcwd(), "aws_screenshot.png")
driver.save_screenshot(screenshot_path)

# Quit driver
driver.quit()

print(f"Screenshot saved to: {screenshot_path}")
