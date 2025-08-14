from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from datetime import datetime

# Set up Chrome options for Jenkins/Docker environment
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open a webpage
driver.get("https://www.amazon.sa") 
time.sleep(5)  # Wait for the page to load

# Create timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
screenshot_filename = f"aws_screenshot_{timestamp}.png"

# Save to Jenkins workspace
screenshot_path = os.path.join(os.getcwd(), screenshot_filename)
driver.save_screenshot(screenshot_path)

# Quit driver
driver.quit()

print(f"Screenshot saved to: {screenshot_path}")
