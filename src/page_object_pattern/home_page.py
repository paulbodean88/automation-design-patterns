"""
Description: module providing the implementation of the search class of the object pattern pattern
class declaration.

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.base_page import BasePage


class HomePage(BasePage):
    """
    Search page
    """
    SEARCH_CONTAINER = 'searchInput'
    SEARCH_BUTTON = 'searchButton'
    CREATE_ACCOUNT = 'pt-createaccount'
    LOGIN = 'pt-login'

    def set_search_query(self, query: str):
        """
        Search for a string
        :param query: string you are looking for
        """
        self._driver.find_element_by_id(HomePage.SEARCH_CONTAINER).send_keys(query)

    def check_search(self):
        """
        Click on search button
        """
        return self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).is_displayed()

    def search(self):
        """
        Click on search button
        """
        self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).click()

    def check_login(self):
        """
        Check a UI element is visible
        """
        return self._driver.find_element_by_id(HomePage.LOGIN).is_displayed()

    def login(self):
        """
        Press login button
        """
        self._driver.find_element_by_id(HomePage.LOGIN).click()

    def check_create_account(self):
        """
        Press create account button
        """
        return self._driver.find_element_by_id(HomePage.CREATE_ACCOUNT).is_displayed()

    def create_account(self):
        """
        Press create account button
        """
        self._driver.find_element_by_id(HomePage.CREATE_ACCOUNT).click()
