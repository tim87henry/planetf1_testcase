""" Import unittest for test case creation.
Import MainPage class, which has the functions related to 
the webpage's display checks.
"""
import unittest
from selenium import webdriver
from mainpage import MainPage

# Creating Testcase by subclassing TestCase class from unittest
class PlanetF1(unittest.TestCase):
    
    # Use setUp() to init webdriver and open webpage
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://planetf1.com")

    # Test that checks the various displays on the webpage
    def test_checkDisplay(self):
        # Create instance of MainPage class
        main_page=MainPage(self.driver)
        # Call the required functions from MainPage
        main_page.headline_news_is_displayed()
        main_page.advert_is_displayed()
        main_page.planetf1_logo_is_displayed()
        main_page.social_media_is_displayed()

    # Use tearDown() to quit the webdriver
    def tearDown(self):
        self.driver.quit()
        return super().tearDown()

if __name__=='__main__':
    unittest.main()
