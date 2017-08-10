"""
Description: This module provides the menu page related interactions

@author: Paul Bodean
@date: 10/08/2017
"""
from src.utils import click_retry
from typing import Union
from selenium.webdriver import Chrome, Firefox


class Menu(object):
    """
    A couple of menu actions are implemented in Menu class
    """
    MENU_BUTTON = '#appbar-guide-button > span > span'
    TREND_BUTTON = '//*[@id="trending-guide-item"]/a/span/span[2]/span'
    HISTORY_BUTTON = '//*[@id="history-guide-item"]/a/span/span[2]'
    BROWSE = '//*[@id="guide_builder-guide-item"]/a/span/span[2]/span'

    def __init__(self, driver: Union[Chrome, Firefox]):
        """

        :param driver: browser driver
        :type driver: object
        """
        self.__driver = driver

    def menu_button(self):
        """
        Click on menu
        """
        click_retry(self.__driver, self.MENU_BUTTON, 'css_selector')

    def filter_by_trend(self):
        """
        Sort results by trend
        """
        click_retry(self.__driver, self.TREND_BUTTON, 'xpath')

    def filter_by_history(self):
        """
        Sort results by history
        """
        click_retry(self.__driver, self.HISTORY_BUTTON, 'xpath')

    def browse(self):
        """
        Browse channels
        """
        click_retry(self.__driver, self.BROWSE, 'xpath')
