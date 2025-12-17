"""
Selenium Learning - Level 1: Finding Elements
This example demonstrates different ways to locate elements on a webpage.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def find_elements_example():
    """
    Demonstrates various methods to find elements:
    - By ID
    - By Name
    - By Class Name
    - By Tag Name
    - By Link Text / Partial Link Text
    - By CSS Selector
    - By XPath
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to a test page
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(2)
        
        # Method 1: Find by ID
        username_field = driver.find_element(By.ID, "username")
        print(f"Found element by ID: {username_field.tag_name}")
        
        # Method 2: Find by Name
        password_field = driver.find_element(By.NAME, "password")
        print(f"Found element by Name: {password_field.tag_name}")
        
        # Method 3: Find by Class Name
        button = driver.find_element(By.CLASS_NAME, "radius")
        print(f"Found element by Class Name: {button.text}")
        
        # Method 4: Find by Tag Name
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Found {len(inputs)} input elements by Tag Name")
        
        # Method 5: Find by Link Text
        link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
        print(f"Found link by Link Text: {link.text}")
        
        # Method 6: Find by Partial Link Text
        partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Elemental")
        print(f"Found link by Partial Link Text: {partial_link.text}")
        
        # Method 7: Find by CSS Selector
        css_element = driver.find_element(By.CSS_SELECTOR, "button.radius")
        print(f"Found element by CSS Selector: {css_element.text}")
        
        # Method 8: Find by XPath
        xpath_element = driver.find_element(By.XPATH, "//button[@class='radius']")
        print(f"Found element by XPath: {xpath_element.text}")
        
        # Find multiple elements
        all_links = driver.find_elements(By.TAG_NAME, "a")
        print(f"\nTotal links on page: {len(all_links)}")
        for i, link in enumerate(all_links[:5], 1):  # Show first 5
            print(f"  Link {i}: {link.text}")
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    find_elements_example()

