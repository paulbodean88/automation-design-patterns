"""
Description: Test module for module src/page_object_patter/base_page.py

@author: Paul Bodean
@date: 25/07/2017
"""

from unittest import TestCase

from selenium.webdriver.common.by import By

from src.page_object_pattern.base_page import BasePage
from src.utils import get_selenium_driver


class TestBasePage(TestCase):
    """
    Check page page functionality
    """
    def setUp(self):
        """
        Driver setup
        :return: driver
        :rtype: object
        """
        driver = get_selenium_driver('chrome')
        driver.get('https://www.youtube.com/')
        return BasePage(driver)

    def test_wait_until_valid(self):
        """
        Perform wait based on Youtube logo
        """
        self.setUp().wait_until_valid(By.XPATH, '//*[@id="logo-container"]/span[1]')

    def tearDown(self):
        """
        Quit browser
        """
        self.setUp().quit_browser()
