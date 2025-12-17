"""
Selenium Learning - Level 3: Screenshots and Alerts
This example demonstrates taking screenshots and handling alerts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def screenshots_alerts_example():
    """
    Demonstrates:
    - Taking full page screenshots
    - Taking element screenshots
    - Handling JavaScript alerts
    - Handling confirm dialogs
    - Handling prompt dialogs
    """
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Create screenshots directory if it doesn't exist
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        # Example 1: Full page screenshot
        print("Example 1: Taking full page screenshot")
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()
        
        screenshot_path = os.path.join(screenshots_dir, "full_page.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        
        time.sleep(2)
        
        # Example 2: Element screenshot
        print("\nExample 2: Taking element screenshot")
        login_form = driver.find_element(By.CSS_SELECTOR, "form")
        
        element_screenshot_path = os.path.join(screenshots_dir, "login_form.png")
        login_form.screenshot(element_screenshot_path)
        print(f"Element screenshot saved to: {element_screenshot_path}")
        
        time.sleep(2)
        
        # Example 3: Handling JavaScript Alert
        print("\nExample 3: Handling JavaScript Alert")
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        
        # Click button that triggers alert
        alert_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
        alert_button.click()
        
        # Wait for alert and switch to it
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        print(f"Alert text: {alert.text}")
        
        # Accept alert (click OK)
        alert.accept()
        print("Alert accepted")
        
        # Verify result
        result = driver.find_element(By.ID, "result")
        print(f"Result: {result.text}")
        
        time.sleep(2)
        
        # Example 4: Handling Confirm Dialog
        print("\nExample 4: Handling Confirm Dialog")
        confirm_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
        confirm_button.click()
        
        confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
        print(f"Confirm text: {confirm.text}")
        
        # Dismiss confirm (click Cancel)
        confirm.dismiss()
        print("Confirm dismissed")
        
        result = driver.find_element(By.ID, "result")
        print(f"Result: {result.text}")
        
        time.sleep(2)
        
        # Example 5: Handling Prompt Dialog
        print("\nExample 5: Handling Prompt Dialog")
        prompt_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
        prompt_button.click()
        
        prompt = WebDriverWait(driver, 10).until(EC.alert_is_present())
        print(f"Prompt text: {prompt.text}")
        
        # Send text to prompt
        prompt.send_keys("Hello from Selenium!")
        prompt.accept()
        print("Prompt accepted with text")
        
        result = driver.find_element(By.ID, "result")
        print(f"Result: {result.text}")
        
        time.sleep(2)
        
        # Example 6: Screenshot after interaction
        print("\nExample 6: Screenshot after interaction")
        driver.get("https://the-internet.herokuapp.com/login")
        
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        
        # Screenshot before login
        before_login_path = os.path.join(screenshots_dir, "before_login.png")
        driver.save_screenshot(before_login_path)
        print(f"Screenshot before login: {before_login_path}")
        
        login_button.click()
        time.sleep(2)
        
        # Screenshot after login
        after_login_path = os.path.join(screenshots_dir, "after_login.png")
        driver.save_screenshot(after_login_path)
        print(f"Screenshot after login: {after_login_path}")
        
    finally:
        time.sleep(2)
        driver.quit()
        print(f"\nAll screenshots saved in '{screenshots_dir}' directory")

if __name__ == "__main__":
    screenshots_alerts_example()

