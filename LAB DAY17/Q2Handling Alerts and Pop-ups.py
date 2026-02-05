from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open alert practice page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

time.sleep(2)

# Trigger a JavaScript Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)

alert = driver.switch_to.alert

# Accept the alert and print its message
print("Simple Alert Text:", alert.text)
alert.accept()

time.sleep(2)

# Dismiss a Confirmation Pop-up
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)

confirm_alert = driver.switch_to.alert
print("Confirmation Alert Text:", confirm_alert.text)
confirm_alert.dismiss()  # Clicks Cancel

time.sleep(2)

# Enter text in a Prompt Alert and accept it
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)

prompt_alert = driver.switch_to.alert
print("Prompt Alert Text:", prompt_alert.text)

prompt_alert.send_keys("Karthik")
prompt_alert.accept()

time.sleep(2)

# Verify the result displayed on the page
result_text = driver.find_element(By.ID, "result").text
print("Result Message on Page:", result_text)

if "Karthik" in result_text:
    print("Prompt alert handled successfully!")
else:
    print("Something went wrong!")

time.sleep(3)
driver.quit()
