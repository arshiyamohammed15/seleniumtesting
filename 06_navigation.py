"""
Selenium Learning - Level 2: Browser Navigation
This example demonstrates browser navigation and controls.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def navigation_example():
    """
    Demonstrates browser navigation:
    - Navigating to URLs
    - Browser back/forward
    - Refreshing pages
    - Window management
    - Getting page information
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigation 1: Get (navigate to URL)
        print("Navigating to Google...")
        driver.get("https://www.google.com")
        print(f"Current URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        
        time.sleep(2)
        
        # Navigation 2: Navigate to another page
        print("\nNavigating to GitHub...")
        driver.get("https://github.com")
        print(f"Current URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        
        time.sleep(2)
        
        # Navigation 3: Browser back
        print("\nGoing back...")
        driver.back()
        print(f"Current URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        
        time.sleep(2)
        
        # Navigation 4: Browser forward
        print("\nGoing forward...")
        driver.forward()
        print(f"Current URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        
        time.sleep(2)
        
        # Navigation 5: Refresh page
        print("\nRefreshing page...")
        driver.refresh()
        print("Page refreshed")
        
        time.sleep(2)
        
        # Window Management
        print("\nWindow Management:")
        print(f"Window size: {driver.get_window_size()}")
        print(f"Window position: {driver.get_window_position()}")
        
        # Maximize window
        driver.maximize_window()
        print("Window maximized")
        
        # Set window size
        driver.set_window_size(1024, 768)
        print(f"Window size set to: {driver.get_window_size()}")
        
        # Get page source (HTML)
        page_source_length = len(driver.page_source)
        print(f"\nPage source length: {page_source_length} characters")
        
        # Get current window handle
        current_window = driver.current_window_handle
        print(f"Current window handle: {current_window}")
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    navigation_example()

