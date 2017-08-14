"""
Description:
* An interface is defined for creating an object.
* Comparing to simple factory, subclasses decide which class is instantiated.

@author: Paul Bodean
@date: 12/08/2017
"""
from abc import ABCMeta, abstractmethod
from typing import Union
from selenium.webdriver import Chrome, Firefox

from src.factory.pages.menu import Menu
from src.factory.pages.search import Search


class Component(object):
    """
    Abstract class defining how a tested component will look
    """

    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def get_actions(self, *args):
        pass


class SearchComponent(Component, Search):
    """
    Each new product will implement specific actions
    """

    def set_name(self):
        return 'Youtube search component'

    def get_actions(self, *args: list):
        """
        :type args: list
        """
        if args[0] == 'click_search':
            self.search()
        elif args[0] == 'set_query':
            self.set_query(args[1])
        else:
            raise NotImplemented


class MenuComponent(Component, Menu):
    """
    Menu specific component are implemented
    """

    def set_name(self):
        return 'Youtube menu component'

    def get_actions(self, *args: list):
        """

        :type args: list
        """
        if args[0] == 'click_menu':
            self.menu_button()
        elif args[0] == 'trend':
            self.filter_by_trend()
        elif args[0] == 'history':
            self.filter_by_history()
        elif args[0] == 'browse':
            self.browse()
        else:
            raise NotImplemented


class TemplateTest(metaclass=ABCMeta):
    """
    TestCase abstract class provide a factory method _create_test which should be implemented by concrete classes
    """

    def __init__(self):
        self.sections = dict()
        self.create_test()

    @abstractmethod
    def create_test(self):
        """
        Factory abstract method
        """
        pass

    def get_sections(self) -> dict:
        """

        :return: all section to be tested in a TestCase
        :rtype: list
        """
        return self.sections

    def add_sections(self, section_key: str, section: object):
        """

        :param section_key: section key name
        :type section_key: str
        :param section: a section to be tested
        :type section: object
        :return: all sections to be tested
        :rtype: list
        """
        self.sections.update({section_key: section})


class MenuTest(TemplateTest):
    """
    Implement Test Menu class
    """

    def __init__(self, driver: Union[Chrome, Firefox]):
        """

        :param driver: browser driver
        :type driver: object
        """
        self.__driver = driver
        super().__init__()

    def create_test(self):
        """

        :return: sections to be tested
        :rtype: dict
        """
        self.add_sections('menu', MenuComponent(self.__driver))


class MenuAndSearchTest(TemplateTest):
    """
    Implement a test case for checking menu and search
    """

    def __init__(self, driver: Union[Chrome, Firefox]):
        """

        :param driver: browser driver
        :type driver: object
        """
        self.__driver = driver
        super().__init__()

    def create_test(self):
        """

        :return: sections to be tested
        :rtype: dict
        """
        self.add_sections('menu', MenuComponent(self.__driver))
        self.add_sections('search', SearchComponent(self.__driver))
