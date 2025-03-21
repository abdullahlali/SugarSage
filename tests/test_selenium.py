from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import sys
import os

class TestSugarSageWebsite(unittest.TestCase):
    def setUp(self):
        print("Setting up Chrome options...")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        
        print("Setting up ChromeDriver...")
        service = Service(ChromeDriverManager().install())
        
        try:
            print("Initializing WebDriver...")
            self.driver = webdriver.Chrome(
                service=service,
                options=chrome_options
            )
            print("WebDriver initialized successfully")
        except Exception as e:
            print(f"Error initializing WebDriver: {str(e)}")
            raise
        
    def tearDown(self):
        if hasattr(self, 'driver'):
            print("Quitting WebDriver...")
            self.driver.quit()
            print("WebDriver quit successfully")
        
    def test_simple(self):
        """Simple test to check if browser starts"""
        try:
            print("Starting simple test...")
            print(f"Current working directory: {os.getcwd()}")
            self.driver.get("https://abdullahlali.github.io/SugarSage/")
            print("Page loaded successfully")
            self.assertTrue(True)
            print("Test completed successfully")
        except Exception as e:
            print(f"Test failed with error: {str(e)}")
            raise

if __name__ == "__main__":
    unittest.main() 