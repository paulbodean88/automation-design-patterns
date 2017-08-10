"""
Description: search functionality

@author: Paul Bodean
@date: 10/08/2017
"""
from typing import Union
from selenium.webdriver import Chrome, Firefox


class Search(object):
    """
    Search page methods implementation
    """
    SEARCH_CONTAINER = '//*[@id="masthead-search-term"]'
    SEARCH_BUTTON = '//*[@id="search-btn"]'

    def __init__(self, driver: Union[Chrome, Firefox]):
        """

        :param driver: browser driver
        :type driver: object
        """
        self.__driver = driver

    def search(self):
        """
        Click on search button
        """
        self.__driver.find_element_by_xpath(Search.SEARCH_BUTTON).click()

    def set_query(self, query):
        """
        Set query
        :return:
        :rtype:
        """
        self.__driver.find_element_by_xpath(Search.SEARCH_CONTAINER).send_keys(query)
