"""
Description: Classical implementation of Singleton design pattern in Python
incorporating Selenium webdriver connection

@author: Paul Bodean
@date: 23.01.2018
"""
from selenium import webdriver


class ClassicalSingleton(object):
    """
    Singleton class based on overriding the __new__ method
    """

    def __new__(cls):
        """
        Override __new__ method to control the obj. creation
        :return: Singleton obj.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassicalSingleton, cls).__new__(cls)

        return cls.instance

    @staticmethod
    def get_driver():
        """

        :return: Selenium driver
        """
        return webdriver.Chrome()


