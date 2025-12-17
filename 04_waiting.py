"""
Selenium Learning - Level 2: Waiting Strategies
This example demonstrates different waiting strategies in Selenium.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def waiting_example():
    """
    Demonstrates different waiting strategies:
    - Implicit waits
    - Explicit waits
    - Expected conditions
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Method 1: Implicit Wait
        # Sets a default wait time for all find_element operations
        print("Setting implicit wait to 10 seconds...")
        driver.implicitly_wait(10)
        
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        
        # Method 2: Explicit Wait with WebDriverWait
        # More precise - waits for specific conditions
        print("\nUsing explicit wait...")
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        )
        start_button.click()
        
        # Wait for element to appear
        finish_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "finish"))
        )
        print(f"Dynamic content loaded: {finish_text.text}")
        
        # Method 3: Different Expected Conditions
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        
        start_button = driver.find_element(By.CSS_SELECTOR, "button")
        start_button.click()
        
        # Wait for text to be present in element
        finish_text = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
        )
        print(f"\nText condition met: {finish_text}")
        
        # Wait for element to be visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        print(f"Element is visible: {element.text}")
        
        # Common Expected Conditions:
        # - presence_of_element_located: Element exists in DOM
        # - visibility_of_element_located: Element is visible
        # - element_to_be_clickable: Element is clickable
        # - text_to_be_present_in_element: Text appears in element
        # - title_contains: Page title contains text
        # - alert_is_present: Alert is present
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    waiting_example()

