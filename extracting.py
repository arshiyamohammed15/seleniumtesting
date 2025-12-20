"""
Data Extraction Practice - Selenium Web Scraping
Extract data from websites using Selenium.
Browser will be VISIBLE so you can watch the extraction process.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys


def setup_driver():
    """
    Setup Chrome driver with visible browser.
    
    Returns:
        WebDriver instance
        
    Raises:
        WebDriverException: If driver setup fails
    """
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        # Setup service with webdriver-manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
        print("Make sure Chrome browser is installed and webdriver-manager is installed:")
        print("  pip install selenium webdriver-manager")
        raise


def extract_heading_text(url: str = "https://www.example.com"):
    """
    Extract heading text from a webpage.
    
    Args:
        url: URL to extract from
        
    Returns:
        Heading text or None if not found
    """
    driver = None
    try:
        driver = setup_driver()
        driver.get(url)
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Try to find h1, h2, or h3 if h1 doesn't exist
        try:
            heading = driver.find_element(By.TAG_NAME, "h1")
            return heading.text
        except NoSuchElementException:
            # Try h2 or h3 as fallback
            try:
                heading = driver.find_element(By.TAG_NAME, "h2")
                return heading.text
            except NoSuchElementException:
                try:
                    heading = driver.find_element(By.TAG_NAME, "h3")
                    return heading.text
                except NoSuchElementException:
                    return None
    except TimeoutException:
        print(f"Error: Timeout loading page {url}")
        return None
    except WebDriverException as e:
        print(f"Error: WebDriver exception - {e}")
        return None
    except Exception as e:
        print(f"Error extracting heading: {e}")
        return None
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass


def extract_all_links(url: str = "https://the-internet.herokuapp.com"):
    """
    Extract all links from a webpage.
    
    Args:
        url: URL to extract from
        
    Returns:
        List of dictionaries with link text and href
    """
    driver = None
    links_data = []
    try:
        driver = setup_driver()
        driver.get(url)
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Find all links
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            try:
                text = link.text.strip()
                href = link.get_attribute("href")
                if text:  # Only add links with text
                    links_data.append({"text": text, "href": href or ""})
            except Exception as e:
                # Skip links that cause errors
                continue
        return links_data
    except TimeoutException:
        print(f"Error: Timeout loading page {url}")
        return []
    except WebDriverException as e:
        print(f"Error: WebDriver exception - {e}")
        return []
    except Exception as e:
        print(f"Error extracting links: {e}")
        return []
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass


def extract_page_info(url: str = "https://www.example.com"):
    """
    Extract basic page information.
    
    Args:
        url: URL to extract from
        
    Returns:
        Dictionary with page title and URL
    """
    driver = None
    try:
        driver = setup_driver()
        driver.get(url)
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        
        return {
            "title": driver.title or "",
            "url": driver.current_url or url
        }
    except TimeoutException:
        print(f"Error: Timeout loading page {url}")
        return {"title": "", "url": url}
    except WebDriverException as e:
        print(f"Error: WebDriver exception - {e}")
        return {"title": "", "url": url}
    except Exception as e:
        print(f"Error extracting page info: {e}")
        return {"title": "", "url": url}
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass


if __name__ == "__main__":
    # Test the extraction functions
    print("="*70)
    print("EXTRACTING DATA - TEST EXECUTION")
    print("="*70)
    
    print("\n1. Extracting heading text...")
    heading = extract_heading_text()
    print(f"   Heading: {heading}")
    
    print("\n2. Extracting page info...")
    page_info = extract_page_info()
    print(f"   Title: {page_info.get('title')}")
    print(f"   URL: {page_info.get('url')}")
    
    print("\n3. Extracting links...")
    links = extract_all_links()
    print(f"   Found {len(links)} links")
    for i, link in enumerate(links[:5], 1):
        print(f"   {i}. {link['text'][:50]} -> {link['href']}")
