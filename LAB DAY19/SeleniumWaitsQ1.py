from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Launch browser
driver = webdriver.Firefox()
driver.maximize_window()

# --------------------------------------------------
# 1️⃣ IMPLICIT WAIT
# --------------------------------------------------
driver.implicitly_wait(10)  # Applies globally to all elements
print("Implicit wait of 10 seconds applied")

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

# --------------------------------------------------
# 2️⃣ EXPLICIT WAIT (Element to be clickable)
# --------------------------------------------------
start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
)
print("Explicit wait: Start button is clickable")
start_button.click()

# --------------------------------------------------
# 3️⃣ FLUENT WAIT (Polling interval)
# --------------------------------------------------
wait = WebDriverWait(
    driver,
    timeout=15,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

hello_text = wait.until(
    EC.presence_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
)

# --------------------------------------------------
# 4️⃣ PRINT MESSAGE WHEN ELEMENT IS AVAILABLE
# --------------------------------------------------
print("Fluent wait: Element is now available for interaction")
print("Text displayed:", hello_text.text)

time.sleep(3)
driver.quit()
