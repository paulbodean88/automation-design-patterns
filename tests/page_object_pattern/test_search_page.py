"""
Description: Test case implementation based on page object pattern and unittest

"""
import unittest

from src.page_object_pattern.search_page import SearchPage
from src.utils import get_selenium_driver


class TestSearchPage(unittest.TestCase):
    """
    Test class for testing a search on Youtube
    """

    def setUp(self):
        """
        Driver setup
        :return: Chrome driver
        :rtype: object
        """
        driver = get_selenium_driver('chrome')
        driver.get('https://www.youtube.com/')
        return driver

    def test_search_string(self):
        """
        Perform searches
        """
        page = SearchPage(self.setUp())
        page.set_search_query('python')
        page.search()
        page.filter_results('Python')

    def tearDown(self):
        """
        Quit browser
        """
        self.setUp().quit()

