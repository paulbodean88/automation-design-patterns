"""
Description:
- Simple Factory Pattern implementation
- To notice the main idea a base class App was created and three other subclasses

@author: Paul Bodean
@date: 10/08/2017
"""

from typing import Union

from selenium.webdriver import Chrome, Firefox


from src.factory.pages.menu import Menu
from src.factory.pages.search import Search
from src.utils import get_selenium_driver


class App(object):
    """

    """

    def __init__(self, driver: Union[Chrome, Firefox]):
        """

        :param driver: browser driver
        :type driver: object
        """
        self.__driver = driver

    def factory(self, page: str):
        """
        The access method which handles pages selection
        :type page: str
        """
        if page == 'Menu':
            return Menu(self.__driver)
        elif page == 'Search':
            return Search(self.__driver)
        else:
            raise NotImplemented

