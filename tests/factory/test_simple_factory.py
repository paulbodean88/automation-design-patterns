"""
Description: Test module for module src/factory/simple_factory.py

@author: Paul Bodean
@date: 10/08/2017
"""

from unittest import TestCase

from src.factory.simple_factory import App
from src.utils import get_selenium_driver


class TestSimpleFactory(TestCase):
    """
    Check simple factory functionality
    """
    def setUp(self):
        """
        Driver + factory setup
        :return: driver
        :rtype: object
        """
        driver = get_selenium_driver('chrome')
        driver.set_window_size(1200, 800)
        driver.get('https://www.youtube.com/')
        return driver, App(driver)

    def test_factory(self):
        """
        Perform some clicks and search for a song
        """
        app = self.setUp()[1]
        # Play around with menu specific ui elements
        app.factory('Menu').menu_button()
        app.factory('Menu').filter_by_history()
        app.factory('Menu').menu_button()
        app.factory('Menu').filter_by_trend()
        app.factory('Menu').menu_button()
        app.factory('Menu').browse()
        # Play around with search specific ui elements
        app.factory('Search').set_query('Miss California')
        app.factory('Search').search()

    def tearDown(self):
        """
        Quit browser
        """
        self.setUp()[0].quit()
