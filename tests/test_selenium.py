from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class TestSugarSageWebsite(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_simple(self):
        """Simple test to check if browser starts"""
        self.driver.get("https://abdullahlali.github.io/SugarSage/")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main() 