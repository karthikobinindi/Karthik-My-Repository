from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# ---------------- IFRAME HANDLING ----------------
driver.get("https://demo.automationtesting.in/Frames.html")

# Locate iframe properly
iframe = wait.until(EC.presence_of_element_located((By.ID, "singleframe")))

# Switch to iframe
driver.switch_to.frame(iframe)

# Locate input inside iframe
input_box = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
)
input_box.send_keys("Hello iFrame")

print("Text entered inside iframe")

# Switch back to main page
driver.switch_to.default_content()
print("Switched back to main content")

# ---------------- WINDOW HANDLING ----------------
driver.get("https://demo.automationtesting.in/Windows.html")

# Click to open new window
wait.until(EC.element_to_be_clickable((By.XPATH, "//a/button"))).click()

parent_window = driver.current_window_handle
all_windows = driver.window_handles

# Switch and print titles
for window in all_windows:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)

# Close child window
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()
        print("Child window closed")

# Return to parent window
driver.switch_to.window(parent_window)
print("Returned to parent window")

time.sleep(2)
driver.quit()
