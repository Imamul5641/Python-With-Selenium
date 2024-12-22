# 1. Open Web Browser(Chrome/Safari)
# 2. Open url https://opensource-demo.orangehrmlive.com/
# 3. Enter Username (Admin).
# 4. Enter password (admin123)
# 5. Click on login
# 6. Capture title of the home page. (Actual title)
# 7. Verify title of the page: OrangeHRM (Expected)
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
# driver = webdriver.Chrome(chrome_driver_path)

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#selenium 3
# driver.find_element_by_name("username").send_keys("Admin")
# driver.find_element_by_name("password").send_keys("admin123")
# driver.find_element_by_class_name("orangehrm-login-button").click()

# Wait for the username field to be visible
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")

# Wait for the password field to be visible
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")

# Wait for the login button to be clickable and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))).click()

# Capture the title of the home page
actual_title = driver.title
print(f"Actual title: {actual_title}")

# Verify the title of the page
expected_title = "OrangeHRM"
if actual_title == expected_title:
    print("Title verification successful!")
else:
    print("Title verification failed!")

# Add a pause to keep the browser open
time.sleep(60)  # Keeps the browser open for 10 seconds

# Close the browser
driver.quit()