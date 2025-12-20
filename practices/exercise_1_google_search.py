"""
Exercise 1: Google Search
Practice navigating to Google and performing a search with visible browser.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_driver():
    """Setup Chrome driver with visible browser (maximized)"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize window
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


def exercise_1_google_search():
    """Practice: Navigate to Google and perform a search"""
    print("\n=== Exercise 1: Google Search ===")
    driver = setup_driver()
    
    try:
        print("Opening Google...")
        driver.get("https://www.google.com")
        time.sleep(2)
        
        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        print("Found search box!")
        
        # Type and search
        search_box.send_keys("Selenium Python tutorial")
        print("Typed search query...")
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)
        print("Searching...")
        
        # Wait for results
        time.sleep(3)
        
        # Get search results
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        print(f"\nFound {len(results)} search results:")
        for i, result in enumerate(results[:5], 1):
            if result.text:
                print(f"  {i}. {result.text}")
        
        time.sleep(3)
        
    finally:
        print("Closing browser...")
        driver.quit()


if __name__ == "__main__":
    exercise_1_google_search()

