"""
Selenium Learning - Level 2: Working with Forms
This example demonstrates how to interact with various form elements.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

def forms_example():
    """
    Demonstrates form interactions:
    - Text inputs
    - Checkboxes
    - Radio buttons
    - Dropdowns/Select elements
    - File uploads
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Example 1: Text inputs and checkboxes
        print("Example 1: Text inputs and checkboxes")
        driver.get("https://the-internet.herokuapp.com/login")
        
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()
        
        time.sleep(2)
        
        # Example 2: Checkboxes
        print("\nExample 2: Working with checkboxes")
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        
        # Check if checkbox is selected
        print(f"Checkbox 1 selected: {checkboxes[0].is_selected()}")
        print(f"Checkbox 2 selected: {checkboxes[1].is_selected()}")
        
        # Click checkbox if not selected
        if not checkboxes[0].is_selected():
            checkboxes[0].click()
            print("Clicked checkbox 1")
        
        # Uncheck checkbox 2 if selected
        if checkboxes[1].is_selected():
            checkboxes[1].click()
            print("Unchecked checkbox 2")
        
        time.sleep(2)
        
        # Example 3: Dropdown/Select elements
        print("\nExample 3: Working with dropdowns")
        driver.get("https://the-internet.herokuapp.com/dropdown")
        
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        
        # Get all options
        options = dropdown.options
        print(f"Total options: {len(options)}")
        for option in options:
            print(f"  Option: {option.text} (value: {option.get_attribute('value')})")
        
        # Select by visible text
        dropdown.select_by_visible_text("Option 2")
        print(f"\nSelected: {dropdown.first_selected_option.text}")
        
        # Select by value
        dropdown.select_by_value("1")
        print(f"Selected: {dropdown.first_selected_option.text}")
        
        # Select by index
        dropdown.select_by_index(2)
        print(f"Selected: {dropdown.first_selected_option.text}")
        
        time.sleep(2)
        
        # Example 4: Radio buttons
        print("\nExample 4: Working with radio buttons")
        driver.get("https://the-internet.herokuapp.com/radio_buttons")
        
        radio_buttons = driver.find_elements(By.NAME, "radio")
        
        for i, radio in enumerate(radio_buttons, 1):
            print(f"Radio {i}: {radio.get_attribute('value')} - Selected: {radio.is_selected()}")
        
        # Select a radio button
        if not radio_buttons[1].is_selected():
            radio_buttons[1].click()
            print(f"\nSelected radio button: {radio_buttons[1].get_attribute('value')}")
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    forms_example()

