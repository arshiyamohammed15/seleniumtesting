"""
Selenium Learning - Level 3: Advanced Actions
This example demonstrates ActionChains for complex interactions.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def actions_chains_example():
    """
    Demonstrates ActionChains for:
    - Mouse hover
    - Drag and drop
    - Right-click (context click)
    - Double-click
    - Keyboard combinations
    - Click and hold
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    actions = ActionChains(driver)
    
    try:
        # Example 1: Mouse hover
        print("Example 1: Mouse hover")
        driver.get("https://the-internet.herokuapp.com/hovers")
        
        # Find avatar elements
        avatars = driver.find_elements(By.CSS_SELECTOR, ".figure")
        
        # Hover over first avatar
        actions.move_to_element(avatars[0]).perform()
        time.sleep(1)
        
        # Check if user info appears
        user_info = driver.find_element(By.CSS_SELECTOR, ".figcaption h5")
        print(f"User info on hover: {user_info.text}")
        
        time.sleep(2)
        
        # Example 2: Drag and drop
        print("\nExample 2: Drag and drop")
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        
        box_a = driver.find_element(By.ID, "column-a")
        box_b = driver.find_element(By.ID, "column-b")
        
        print(f"Box A text before: {box_a.text}")
        print(f"Box B text before: {box_b.text}")
        
        # Perform drag and drop
        actions.drag_and_drop(box_a, box_b).perform()
        
        time.sleep(1)
        
        # Verify swap
        box_a = driver.find_element(By.ID, "column-a")
        box_b = driver.find_element(By.ID, "column-b")
        print(f"Box A text after: {box_a.text}")
        print(f"Box B text after: {box_b.text}")
        
        time.sleep(2)
        
        # Example 3: Right-click (context click)
        print("\nExample 3: Right-click")
        driver.get("https://the-internet.herokuapp.com/context_menu")
        
        hot_spot = driver.find_element(By.ID, "hot-spot")
        
        # Right-click on element
        actions.context_click(hot_spot).perform()
        time.sleep(1)
        
        # Handle alert
        alert = driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()
        
        time.sleep(2)
        
        # Example 4: Double-click
        print("\nExample 4: Double-click")
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("selenium")
        
        # Double-click to select all text
        actions.double_click(search_box).perform()
        time.sleep(1)
        
        # Type new text (replaces selected text)
        search_box.send_keys("python")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        # Example 5: Keyboard combinations
        print("\nExample 5: Keyboard combinations")
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        
        # Ctrl+A (select all)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(1)
        
        # Type new search
        search_box.send_keys("webdriver")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        # Example 6: Click and hold
        print("\nExample 6: Click and hold")
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        
        box_a = driver.find_element(By.ID, "column-a")
        box_b = driver.find_element(By.ID, "column-b")
        
        # Click and hold, then move
        actions.click_and_hold(box_a).move_to_element(box_b).release().perform()
        
        time.sleep(2)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    actions_chains_example()

