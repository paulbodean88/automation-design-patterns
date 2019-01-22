import abc

from src.utils import get_selenium_driver


class TestManager:
    """
    Control the construction process, having a builder associated with it
    It delegates to the builder the implementation details,
    and deliver the already implemented functionality to the client
    """

    __builder = None
    __status = True

    def set_manager(self, builder):
        """
        Selection of the builder which will construct the product
        :param builder: concrete builder which will implement the product
        """

        self.__builder = builder

    def get_test(self):
        """
        Prepare the test product to be delivered to a client
        """

        # Pre validation
        pre_validation = self.__builder.get_pre_validation()
        # Set flow
        if pre_validation:
            self.__builder.get_flow()
            # Make comparison
            if self.__builder.get_post_validation():
                self.__status = True
            else:
                self.__status = False

        else:
            self.__status = False
        # Post results
        self.__builder.get_report(self.__status)
        # Close driver
        self.__builder.close()


class Test:
    """
    Represent the complex object under construction.
    """

    def __init__(self):
        pass


class Builder(metaclass=abc.ABCMeta):
    """
    Abstract interface for defining parts of the Product
    """

    def __init__(self):
        self._driver = get_selenium_driver('chrome')
        self.product = Test()
        self._driver.get('https://en.wikipedia.org/')

    @abc.abstractmethod
    def get_pre_validation(self):
        pass

    @abc.abstractmethod
    def get_flow(self):
        pass

    @abc.abstractmethod
    def get_post_validation(self):
        pass

    @abc.abstractmethod
    def get_report(self, status):
        pass

    def close(self):
        self._driver.quit()


class SearchFlow(Builder):
    """
    Definition of a concrete builder
    """
    SEARCH_CONTAINER = 'searchInput'
    SEARCH_BUTTON = 'searchButton'
    CREATE_ACCOUNT = 'pt-createaccount'
    LOGIN = 'pt-login'
    HEADING = 'firstHeading'

    def get_pre_validation(self):
        """
        Validate if UI is available for the environment to be tested
        :return: True or False
        """
        return self._driver.find_element_by_id('p-search').is_displayed()

    def get_flow(self):
        """

        :return: True if validation succeeded
        """
        self._driver.find_element_by_id(SearchFlow.SEARCH_CONTAINER).send_keys('Design patterns')
        self._driver.find_element_by_id(SearchFlow.SEARCH_BUTTON).click()

    def get_post_validation(self):
        """

        :return: True if flow was executed
        """
        return self._driver.find_element_by_id(SearchFlow.HEADING).text == 'Design pattern'

    def get_report(self, status):
        print("Test execution:", status)
