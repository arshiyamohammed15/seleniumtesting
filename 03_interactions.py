"""
Selenium Learning - Level 1: Basic Interactions
This example demonstrates how to interact with web elements.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def interactions_example():
    """
    Demonstrates basic interactions:
    - Clicking elements
    - Typing text
    - Clearing fields
    - Keyboard actions
    - Getting element attributes and text
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to a test page
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(2)
        
        # Find elements
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        
        # Interaction 1: Clear a field
        print("Clearing username field...")
        username_field.clear()
        
        # Interaction 2: Type text
        print("Typing username...")
        username_field.send_keys("tomsmith")
        
        # Interaction 3: Type password
        print("Typing password...")
        password_field.send_keys("SuperSecretPassword!")
        
        # Interaction 4: Click button
        print("Clicking login button...")
        login_button.click()
        
        time.sleep(2)
        
        # Check if login was successful
        success_message = driver.find_element(By.ID, "flash")
        print(f"\nLogin result: {success_message.text}")
        
        # Interaction 5: Keyboard actions
        print("\nDemonstrating keyboard actions...")
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)  # Press Enter
        
        time.sleep(2)
        
        # Interaction 6: Get element attributes
        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        print(f"\nFirst result text: {first_result.text}")
        print(f"First result tag: {first_result.tag_name}")
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    interactions_example()

