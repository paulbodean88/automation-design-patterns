"""
Description: module providing the implementation of the search class of the object pattern pattern
class declaration.

@author: Paul Bodean
@date: 25/07/2017
"""

from selenium.webdriver.common.by import By
from src.page_object_pattern.base_page import BasePage


class SearchPage(BasePage):
    """
    Search page
    """
    SEARCH_CONTAINER = '//*[@id="masthead-search-term"]'
    SEARCH_BUTTON = '//*[@id="search-btn"]'

    def set_search_query(self, query: str):
        """
        Search for a string
        :param query: string to look for
        :type query: string
        """
        self._driver.find_element_by_xpath(SearchPage.SEARCH_CONTAINER).send_keys(query)

    def search(self):
        """
        Click on search button
        """
        self._driver.find_element_by_xpath(SearchPage.SEARCH_BUTTON).click()

    def filter_results(self, string: str):
        """

        :param string: search for an element containing a specific string
        :type string: str
        """
        self.wait_until_valid(By.PARTIAL_LINK_TEXT, string)
        self._driver.find_elements_by_partial_link_text(string)[0].click()
