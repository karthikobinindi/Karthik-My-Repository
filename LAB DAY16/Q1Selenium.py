from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
time.sleep(2)

# Generate unique email
email = f"testuser{int(time.time())}@gmail.com"

# Fill form
driver.find_element(By.ID, "input-firstname").send_keys("Karthik")
driver.find_element(By.NAME, "lastname").send_keys("obinindi")
driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("9876543210")
driver.find_element(By.ID, "input-password").send_keys("Test@123")
driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

# Agree checkbox
driver.find_element(By.NAME, "agree").click()

# Submit
driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
time.sleep(3)

# Validate success
msg = driver.find_element(By.CSS_SELECTOR, "#content h1").text

if "Your Account Has Been Created" in msg:
    print("✅ Test Passed — Account Created Successfully")
else:
    print("❌ Test Failed")


