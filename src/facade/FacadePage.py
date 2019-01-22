"""
Implement a test flow using facade pattern.
The flow will be a unified high-level interface for all the pages which composes the test app
"""
from src.page_object_pattern.home_page import HomePage
from src.page_object_pattern.search_page import SearchPage
from src.utils import get_selenium_driver


class FacadePage:
    """
    Facade class delegates the client requests to the actual subsystems
    """
    __driver = get_selenium_driver('chrome')

    def get_driver(self):
        """

        :return: selenium driver
        """
        return self.__driver

    @staticmethod
    def get_home_page():
        """
        Implement home page sub-system
        :return: HomePage class
        """
        return HomePage(FacadePage.__driver)

    @staticmethod
    def get_search_page():
        """
        Implement search page sub-system
        :return: SearchPage class
        """
        return SearchPage(FacadePage.__driver)


facade = FacadePage()
driver = facade.get_driver()
driver.get('https://en.wikipedia.org/')
facade.get_home_page().set_search_query('Wiki')
