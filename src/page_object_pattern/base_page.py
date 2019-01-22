"""
Description:
    - module providing the implementation of the base page class of the object pattern pattern.
@author: Paul Bodean
@date: 25/07/2017
"""


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver):
        self._driver = driver
