# Selenium Quick Reference Guide

## Common Imports
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
```

## Setting Up WebDriver
```python
# Using webdriver-manager (recommended)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Manual setup
driver = webdriver.Chrome()

# With options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
```

## Finding Elements

### By ID
```python
element = driver.find_element(By.ID, "username")
```

### By Name
```python
element = driver.find_element(By.NAME, "password")
```

### By Class Name
```python
element = driver.find_element(By.CLASS_NAME, "button")
```

### By Tag Name
```python
elements = driver.find_elements(By.TAG_NAME, "a")
```

### By Link Text
```python
link = driver.find_element(By.LINK_TEXT, "Click Here")
```

### By CSS Selector
```python
element = driver.find_element(By.CSS_SELECTOR, "button.primary")
```

### By XPath
```python
element = driver.find_element(By.XPATH, "//button[@class='primary']")
```

## Basic Interactions

### Click
```python
button.click()
```

### Type Text
```python
input_field.send_keys("text")
```

### Clear Field
```python
input_field.clear()
```

### Get Text
```python
text = element.text
```

### Get Attribute
```python
value = element.get_attribute("value")
href = element.get_attribute("href")
```

## Waiting Strategies

### Implicit Wait
```python
driver.implicitly_wait(10)  # Wait up to 10 seconds
```

### Explicit Wait
```python
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element")))
```

### Common Expected Conditions
- `EC.presence_of_element_located()` - Element exists in DOM
- `EC.visibility_of_element_located()` - Element is visible
- `EC.element_to_be_clickable()` - Element is clickable
- `EC.text_to_be_present_in_element()` - Text appears
- `EC.alert_is_present()` - Alert is present

## Form Elements

### Checkbox
```python
checkbox = driver.find_element(By.ID, "checkbox")
if not checkbox.is_selected():
    checkbox.click()
```

### Radio Button
```python
radio = driver.find_element(By.ID, "radio1")
radio.click()
```

### Dropdown/Select
```python
dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 1")
dropdown.select_by_value("1")
dropdown.select_by_index(0)
```

## Navigation

### Navigate to URL
```python
driver.get("https://example.com")
```

### Browser Controls
```python
driver.back()      # Go back
driver.forward()   # Go forward
driver.refresh()   # Refresh page
```

### Window Management
```python
driver.maximize_window()
driver.set_window_size(1024, 768)
driver.get_window_size()
```

## Frames and Windows

### Switch to Frame
```python
iframe = driver.find_element(By.ID, "iframe")
driver.switch_to.frame(iframe)
driver.switch_to.default_content()  # Switch back
```

### Multiple Windows
```python
main_window = driver.current_window_handle
driver.switch_to.window(window_handle)
driver.close()  # Close current window
```

## ActionChains (Advanced Actions)

### Mouse Hover
```python
actions = ActionChains(driver)
actions.move_to_element(element).perform()
```

### Drag and Drop
```python
actions.drag_and_drop(source, target).perform()
```

### Right Click
```python
actions.context_click(element).perform()
```

### Double Click
```python
actions.double_click(element).perform()
```

## JavaScript Execution

### Execute JavaScript
```python
driver.execute_script("return document.title;")
driver.execute_script("arguments[0].click();", element)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
```

### Scroll
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Bottom
driver.execute_script("window.scrollTo(0, 0);")  # Top
```

## Screenshots

### Full Page Screenshot
```python
driver.save_screenshot("screenshot.png")
```

### Element Screenshot
```python
element.screenshot("element.png")
```

## Alerts

### Handle Alert
```python
alert = driver.switch_to.alert
print(alert.text)
alert.accept()    # Click OK
alert.dismiss()   # Click Cancel
alert.send_keys("text")  # For prompts
```

## Best Practices

1. **Always use explicit waits** instead of `time.sleep()`
2. **Use unique locators** (ID > Name > CSS > XPath)
3. **Handle exceptions** properly
4. **Clean up resources** with `driver.quit()` in finally block
5. **Use Page Object Model** for larger projects
6. **Take screenshots** on failures for debugging
7. **Use headless mode** for CI/CD pipelines

## Common Patterns

### Setup and Teardown
```python
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

def teardown(driver):
    driver.quit()

# Usage
driver = setup()
try:
    # Your test code
    pass
finally:
    teardown(driver)
```

### Wait for Element and Click
```python
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "button")))
button.click()
```

### Fill Form
```python
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("user")
password.send_keys("pass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
```

