from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestSugarSageWebsite(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://sugarsage.github.io/")  # Replace with your actual GitHub Pages URL
        
    def tearDown(self):
        self.driver.quit()
        
    def test_page_title(self):
        """Test if the page title is correct"""
        self.assertIn("SugarSage", self.driver.title)
        
    def test_navigation(self):
        """Test if main navigation elements are present"""
        nav_elements = self.driver.find_elements(By.TAG_NAME, "nav")
        self.assertTrue(len(nav_elements) > 0)
    
    
    def test_api_endpoint(self):
        """Test if the backend API is responding"""
        try:
            # Wait for API response element to be present
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "api-response"))
            )
            api_response = self.driver.find_element(By.CLASS_NAME, "api-response")
            self.assertIsNotNone(api_response)
        except:
            self.fail("API response not received")

    def test_navigation_links(self):
        """Test if all navigation links are working"""
        try:
            nav_links = self.driver.find_elements(By.CSS_SELECTOR, "nav a")
            for link in nav_links:
                href = link.get_attribute("href")
                self.assertIsNotNone(href, "Navigation link has no href attribute")
                self.assertNotEqual(href, "", "Navigation link href is empty")
        except:
            self.fail("Navigation links test failed")

if __name__ == "__main__":
    unittest.main() 