import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_google(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

        # Find the search box, enter 'Python', and submit the form
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python")
        search_box.send_keys(Keys.RETURN)

        # Wait a few seconds to see the results
        time.sleep(10)

        # Check if 'python.org' is in the search results
        self.assertIn("python.org", driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()