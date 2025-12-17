"""
Selenium Learning - Level 4: Real-world Test Example
Complete login flow test with assertions and error handling.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class LoginTest:
    """Example test class for login functionality"""
    
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def setup(self):
        """Setup WebDriver and wait object"""
        print("Setting up test...")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def teardown(self):
        """Clean up after test"""
        print("Cleaning up...")
        if self.driver:
            self.driver.quit()
    
    def test_successful_login(self):
        """Test successful login scenario"""
        print("\n=== Test: Successful Login ===")
        
        try:
            # Navigate to login page
            self.driver.get("https://the-internet.herokuapp.com/login")
            
            # Find elements
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
            
            # Enter credentials
            username_field.send_keys("tomsmith")
            password_field.send_keys("SuperSecretPassword!")
            
            # Click login
            login_button.click()
            
            # Wait for success message
            success_message = self.wait.until(
                EC.presence_of_element_located((By.ID, "flash"))
            )
            
            # Assertions
            assert "You logged into a secure area!" in success_message.text, \
                "Login success message not found"
            
            assert "/secure" in self.driver.current_url, \
                "Not redirected to secure area"
            
            print("✓ Login successful!")
            print(f"  Success message: {success_message.text}")
            print(f"  Current URL: {self.driver.current_url}")
            
            return True
            
        except Exception as e:
            print(f"✗ Test failed: {str(e)}")
            return False
    
    def test_failed_login(self):
        """Test failed login scenario"""
        print("\n=== Test: Failed Login ===")
        
        try:
            # Navigate to login page
            self.driver.get("https://the-internet.herokuapp.com/login")
            
            # Find elements
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
            
            # Enter wrong credentials
            username_field.send_keys("wrong_user")
            password_field.send_keys("wrong_password")
            
            # Click login
            login_button.click()
            
            # Wait for error message
            error_message = self.wait.until(
                EC.presence_of_element_located((By.ID, "flash"))
            )
            
            # Assertions
            assert "Your username is invalid!" in error_message.text, \
                "Error message not found"
            
            assert "/login" in self.driver.current_url, \
                "Should remain on login page"
            
            print("✓ Failed login handled correctly!")
            print(f"  Error message: {error_message.text}")
            
            return True
            
        except Exception as e:
            print(f"✗ Test failed: {str(e)}")
            return False
    
    def test_logout(self):
        """Test logout functionality"""
        print("\n=== Test: Logout ===")
        
        try:
            # First login
            self.driver.get("https://the-internet.herokuapp.com/login")
            
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
            
            username_field.send_keys("tomsmith")
            password_field.send_keys("SuperSecretPassword!")
            login_button.click()
            
            # Wait for secure area
            self.wait.until(EC.url_contains("/secure"))
            
            # Find and click logout button
            logout_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary"))
            )
            logout_button.click()
            
            # Verify logout
            logout_message = self.wait.until(
                EC.presence_of_element_located((By.ID, "flash"))
            )
            
            assert "You logged out of the secure area!" in logout_message.text, \
                "Logout message not found"
            
            assert "/login" in self.driver.current_url, \
                "Not redirected to login page"
            
            print("✓ Logout successful!")
            print(f"  Logout message: {logout_message.text}")
            
            return True
            
        except Exception as e:
            print(f"✗ Test failed: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all test methods"""
        self.setup()
        
        try:
            results = []
            results.append(self.test_successful_login())
            time.sleep(2)
            
            results.append(self.test_failed_login())
            time.sleep(2)
            
            results.append(self.test_logout())
            
            # Summary
            print("\n" + "="*50)
            print("TEST SUMMARY")
            print("="*50)
            passed = sum(results)
            total = len(results)
            print(f"Passed: {passed}/{total}")
            
            if all(results):
                print("✓ All tests passed!")
            else:
                print("✗ Some tests failed")
            
        finally:
            self.teardown()

if __name__ == "__main__":
    test = LoginTest()
    test.run_all_tests()

