from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1️⃣ Open example.com
driver.get("https://example.com")
time.sleep(2)
print("Initial Page Title:", driver.title)

# 2️⃣ Navigate to another page on same site (reload via URL variation)
driver.get("https://example.com/")
time.sleep(2)
print("Navigated Page Title:", driver.title)

# 3️⃣ Browser Navigation Actions

# Back
driver.back()
time.sleep(2)
print("After Back Title:", driver.title)

# Forward
driver.forward()
time.sleep(2)
print("After Forward Title:", driver.title)

# Refresh
driver.refresh()
time.sleep(2)
print("After Refresh Title:", driver.title)

# 5️⃣ Close the browser
driver.quit()
