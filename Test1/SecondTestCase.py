# 1. Open Web Browser(Chrome/Safari)
# 2. Open url https://admin-demo.nopcommerce.com/login
# 3. Provide Email (admin@yourstore.com).
# 4. Provide password (admin)
# 5. Click on login
# 6. Capture title of the dashboard page. (Actual title)
# 7. Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
# 8. Close Browser

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the path to ChromeDriver
chrome_driver_path = "/Users/imamulhasan/downloads/chromedriver-mac-x64/chromedriver"

# # Configure ChromeDriver service
service = Service(chrome_driver_path)

# Launch the browser using the service
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("https://admin-demo.nopcommerce.com/login")

# # Wait for the username field to be visible
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Email"))).send_keys("admin@yourstore.com")
#
# # Wait for the password field to be visible
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Password"))).send_keys("admin")

# Wait for the login button to be clickable and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))).click()

# Capture the title of the home page
actual_title = driver.title
print(f"Actual title: {actual_title}")

# Verify the title of the page
expected_title = "Dashboard / nopCommerce administration"
if actual_title == expected_title:
    print("Title verification successful!")
else:
    print("Title verification failed!")

# Add a pause to keep the browser open
time.sleep(5)  # Keeps the browser open for 5 seconds

# Close the browser
driver.quit()