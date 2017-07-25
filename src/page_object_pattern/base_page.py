"""
Description:
    - module providing the implementation of the base page class of the object pattern pattern.
Methods:
    - wait_unit_valid
    - quit browser

@author: Paul Bodean
@date: 25/07/2017
"""

from typing import Union

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome, Firefox


class BasePage(object):
    """
    Page object pattern base class
    """

    def __init__(self, selenium_driver: Union[Chrome, Firefox]):
        """

        :param selenium_driver: browser driver
        :type selenium_driver: Union
        """
        self._driver = selenium_driver

    def wait_until_valid(self, category, string):
        """
        Wait for an element to be visible
        :param category:
        :type category:
        :param string:
        :type string:
        :return:
        :rtype:
        """
        WebDriverWait(self._driver, 3).until(
            expected_conditions.presence_of_element_located((category, string))
        )

    def quit_browser(self):
        """
        Quit the browser
        """
        self._driver.quit()
