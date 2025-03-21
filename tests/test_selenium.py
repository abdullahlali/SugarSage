import unittest
import os
import sys

class TestSugarSageWebsite(unittest.TestCase):
    def test_simple(self):
        """Simple test to check if imports work"""
        print("Python version:", sys.version)
        print("Current directory:", os.getcwd())
        print("Directory contents:", os.listdir())
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main() 