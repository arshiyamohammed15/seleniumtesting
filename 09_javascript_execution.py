"""
Selenium Learning - Level 3: JavaScript Execution
This example demonstrates executing JavaScript in Selenium.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def javascript_execution_example():
    """
    Demonstrates JavaScript execution for:
    - Scrolling
    - Changing element properties
    - Getting element values
    - Executing custom JavaScript
    - Highlighting elements
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Example 1: Scroll to element
        print("Example 1: Scrolling to element")
        driver.get("https://the-internet.herokuapp.com/large")
        
        # Find element at bottom
        element = driver.find_element(By.ID, "large-table")
        
        # Scroll element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print("Scrolled to element")
        
        time.sleep(2)
        
        # Example 2: Scroll to bottom of page
        print("\nExample 2: Scroll to bottom")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scrolled to bottom")
        
        time.sleep(2)
        
        # Example 3: Scroll to top
        print("\nExample 3: Scroll to top")
        driver.execute_script("window.scrollTo(0, 0);")
        print("Scrolled to top")
        
        time.sleep(2)
        
        # Example 4: Get page title with JavaScript
        print("\nExample 4: Getting values with JavaScript")
        title = driver.execute_script("return document.title;")
        print(f"Page title (via JS): {title}")
        
        # Get page URL
        url = driver.execute_script("return window.location.href;")
        print(f"Page URL (via JS): {url}")
        
        # Example 5: Change element style (highlight)
        print("\nExample 5: Highlighting element")
        driver.get("https://the-internet.herokuapp.com/login")
        
        username_field = driver.find_element(By.ID, "username")
        
        # Highlight element with yellow background
        driver.execute_script(
            "arguments[0].style.backgroundColor = 'yellow';",
            username_field
        )
        print("Element highlighted")
        
        time.sleep(2)
        
        # Remove highlight
        driver.execute_script(
            "arguments[0].style.backgroundColor = '';",
            username_field
        )
        
        # Example 6: Set element value
        print("\nExample 6: Setting value with JavaScript")
        driver.execute_script(
            "arguments[0].value = 'test_user';",
            username_field
        )
        print(f"Username field value: {username_field.get_attribute('value')}")
        
        # Example 7: Click element with JavaScript
        print("\nExample 7: Clicking with JavaScript")
        password_field = driver.find_element(By.ID, "password")
        driver.execute_script("arguments[0].value = 'test_password';", password_field)
        
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        driver.execute_script("arguments[0].click();", login_button)
        
        time.sleep(2)
        
        # Example 8: Get element text with JavaScript
        print("\nExample 8: Getting element text")
        flash_message = driver.find_element(By.ID, "flash")
        text = driver.execute_script("return arguments[0].textContent;", flash_message)
        print(f"Flash message text: {text.strip()}")
        
        # Example 9: Execute complex JavaScript
        print("\nExample 9: Complex JavaScript")
        result = driver.execute_script("""
            return {
                title: document.title,
                url: window.location.href,
                width: window.innerWidth,
                height: window.innerHeight
            };
        """)
        print(f"Page info: {result}")
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    javascript_execution_example()

