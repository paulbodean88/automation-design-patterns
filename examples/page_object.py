"""
Test case implementation to be added here
"""
import unittest

from src.page_object_pattern.search_page import SearchPage
from src.utils import get_selenium_driver


class TestSearch(unittest.TestCase):
    """
    Simple search on Youtube page on page object pattern based on unittest
    """

    def setUp(self):
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
        self.setUp().quit()

