"""
Selenium Learning - Level 3: Frames and Multiple Windows
This example demonstrates handling frames and multiple browser windows.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def frames_windows_example():
    """
    Demonstrates:
    - Switching between frames
    - Handling multiple windows/tabs
    - Window handles
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Example 1: Working with frames
        print("Example 1: Working with frames")
        driver.get("https://the-internet.herokuapp.com/iframe")
        
        # Switch to frame by name or ID
        iframe = driver.find_element(By.ID, "mce_0_ifr")
        driver.switch_to.frame(iframe)
        
        # Now we're inside the frame, interact with elements
        editor = driver.find_element(By.ID, "tinymce")
        print(f"Editor text before: {editor.text}")
        
        # Clear and type new text
        editor.clear()
        editor.send_keys("Hello from Selenium! This text is inside an iframe.")
        print(f"Editor text after: {editor.text}")
        
        # Switch back to default content (main page)
        driver.switch_to.default_content()
        print("Switched back to main page")
        
        time.sleep(2)
        
        # Example 2: Multiple windows/tabs
        print("\nExample 2: Handling multiple windows")
        driver.get("https://the-internet.herokuapp.com/windows")
        
        # Get current window handle
        main_window = driver.current_window_handle
        print(f"Main window handle: {main_window}")
        
        # Click link that opens new window
        link = driver.find_element(By.LINK_TEXT, "Click Here")
        link.click()
        
        # Wait for new window to open
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        
        # Get all window handles
        all_windows = driver.window_handles
        print(f"Total windows: {len(all_windows)}")
        
        # Switch to new window
        for window in all_windows:
            if window != main_window:
                driver.switch_to.window(window)
                print(f"Switched to new window: {window}")
                print(f"New window title: {driver.title}")
                print(f"New window URL: {driver.current_url}")
                
                # Interact with new window
                new_window_text = driver.find_element(By.TAG_NAME, "h3")
                print(f"New window content: {new_window_text.text}")
                
                # Close new window
                driver.close()
                break
        
        # Switch back to main window
        driver.switch_to.window(main_window)
        print(f"\nSwitched back to main window: {driver.title}")
        
        time.sleep(2)
        
        # Example 3: Opening new tab with JavaScript
        print("\nExample 3: Opening new tab")
        driver.execute_script("window.open('https://www.google.com', '_blank');")
        
        # Wait for new tab
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        
        # Switch to new tab
        all_windows = driver.window_handles
        for window in all_windows:
            if window != main_window:
                driver.switch_to.window(window)
                print(f"Switched to new tab: {driver.title}")
                driver.close()
                break
        
        # Back to main window
        driver.switch_to.window(main_window)
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    frames_windows_example()

