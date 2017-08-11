"""
Description:
- Simple Factory Pattern implementation
- To notice them main idea a base class App was created and two other subclasses

@author: Paul Bodean
@date: 10/08/2017
"""

from typing import Union

from selenium.webdriver import Chrome, Firefox

from src.factory.pages.menu import Menu
from src.factory.pages.search import Search


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
