"""
Selenium Learning - Level 1: Basic Setup
This example demonstrates how to set up Selenium WebDriver and open a browser.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def basic_setup_example():
    """
    Basic example showing how to:
    1. Set up Chrome WebDriver
    2. Open a webpage
    3. Get page title
    4. Close the browser
    """
    
    # Method 1: Using webdriver-manager (Recommended - handles driver automatically)
    print("Setting up Chrome WebDriver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Method 2: Manual setup (if you have driver in PATH)
    # driver = webdriver.Chrome()
    
    # Method 3: With custom options
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run without opening browser
    # chrome_options.add_argument("--start-maximized")  # Maximize window
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # Navigate to a webpage
        print("Opening webpage...")
        driver.get("https://www.google.com")
        
        # Get page title
        title = driver.title
        print(f"Page title: {title}")
        
        # Get current URL
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        
        # Wait a bit to see the page (for learning purposes)
        import time
        time.sleep(3)
        
    finally:
        # Always close the browser
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    basic_setup_example()

