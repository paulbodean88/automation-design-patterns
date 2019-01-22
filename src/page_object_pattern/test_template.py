"""
Description:
    - Test Template class.
Methods:
    - test setup
    - test teardown
    - test implementation

@author: Paul Bodean
@date: 26/12/2017
"""

import unittest
from selenium import webdriver


class TestTemplate(unittest.TestCase):
    def setUp(self):
        """
        Open the page to be tested
        :return: the driver implementation
        """

        self.driver = webdriver.Chrome()
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")

    def tearDown(self):
        """
        Quit the browser
        """
        self.driver.quit()
