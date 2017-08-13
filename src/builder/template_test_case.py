"""
A test template class to emphasize the help of the builder pattern in automation work.
"""

from selenium.webdriver import Chrome
from time import sleep


class TestTemplate(object):
    """
    Generic test case template.
    It exposes a set of actions that are required for the most basic interactions.

    All the methods are designed to add an action to the instance attribute 'actions'
    The list contains tuples of 2, where the first position represents a callback to a driver method
    and the second position is a list of method arguments.
    """

    def __init__(self, driver: Chrome):
        """
        Constructor.
        :param driver: a connection driver from the Selenium package.
        :type driver: Chrome
        """
        self.__driver = driver
        self.__actions = []

    def click_element(self, element_xpath):
        """
        Generic method for clicking an element given by xpath.
        :param element_xpath: the xpath identifier for the element.
        :type element_xpath: str

        It appends a tuple with the 'click' method of the retrieved element and an empty list of args.
        """
        self.__actions.append((self.__driver.find_element_by_xpath(element_xpath).click, []))

    def type_text(self, element_xpath, text):
        """
        Generic method used for typing text in a text box.
        :param element_xpath: the xpath identifier of the text box.
        :type element_xpath: str
        :param text: the text to type.
        :type text: str

        It appends a tuple with the 'send_keys' method of the retrieved element and a list with the args
        in this case the text value.
        """
        self.__actions.append((self.__driver.find_element_by_xpath(element_xpath).send_keys, [text]))

    def wait(self, seconds):
        """
        Generic method to wait.
        :param seconds: the amount of time to wait in seconds.
        :type seconds: int
        """
        self.__actions.append((sleep, [seconds]))

    def compare_text(self, element_xpath, text):
        """
        Generic method to assert the text of an element.
        :param element_xpath: the xpath identifier of the element.
        :type element_xpath: str
        :param text: the reference text
        :type text: str
        """
        self.__actions.append((TestTemplate.__is_equal,
                               [self.__driver.find_element_by_xpath(element_xpath).text, text]))

    def execute_test(self):
        """
        Terminal method that executes all the added methods.
        :return:
        :rtype:
        """
        for action, args in self.__actions:
            action(*args)

    @staticmethod
    def __is_equal(actual, reference):
        assert actual == reference