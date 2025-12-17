"""
Selenium Learning - Level 4: Using Selenium with pytest
This example shows how to structure Selenium tests with pytest framework.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage:
    """Test class for login page functionality"""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        # Setup
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        yield  # Test runs here
        
        # Teardown
        self.driver.quit()
    
    def test_page_loads(self):
        """Test that login page loads correctly"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        # Verify page title
        assert "The Internet" in self.driver.title
        
        # Verify login form elements are present
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
        
        assert username_field.is_displayed()
        assert password_field.is_displayed()
        assert login_button.is_displayed()
    
    def test_successful_login(self):
        """Test successful login"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
        
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        login_button.click()
        
        # Verify success
        success_message = self.wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        
        assert "You logged into a secure area!" in success_message.text
        assert "/secure" in self.driver.current_url
    
    def test_invalid_username(self):
        """Test login with invalid username"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
        
        username_field.send_keys("invalid_user")
        password_field.send_keys("SuperSecretPassword!")
        login_button.click()
        
        error_message = self.wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        
        assert "Your username is invalid!" in error_message.text
    
    def test_invalid_password(self):
        """Test login with invalid password"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
        
        username_field.send_keys("tomsmith")
        password_field.send_keys("wrong_password")
        login_button.click()
        
        error_message = self.wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        
        assert "Your password is invalid!" in error_message.text
    
    @pytest.mark.parametrize("username,password,expected_message", [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("wrong_user", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "wrong_pass", "Your password is invalid!"),
    ])
    def test_login_scenarios(self, username, password, expected_message):
        """Parameterized test for multiple login scenarios"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        message = self.wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        
        assert expected_message in message.text

# To run these tests, use:
# pytest 12_pytest_example.py -v
# pytest 12_pytest_example.py::TestLoginPage::test_successful_login -v
# pytest 12_pytest_example.py -k "login" -v

