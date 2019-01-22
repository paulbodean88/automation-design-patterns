"""
Description: Singleton implementation using decorators

@author: Paul Bodean
@date: 23.01.2018
"""

from selenium import webdriver
from singleton_decorator import singleton


def my_singleton(*args):
    """

    :param cls: class to be changed as a singleton
    :return: instance of the singleton
    """
    instances = dict()

    def get_instance():
        if args[0] not in instances:
            instances[args[0]] = args[0]()
        # else: #uncomment this part in order to raise a warning related to instantiation
        #     raise UserWarning("An instantiation already exists!")
        return instances[args[0]]

    return get_instance


@my_singleton
class MyDriver:
    @staticmethod
    def get_driver():
        return webdriver.Chrome()


@singleton
class Driver:
    @staticmethod
    def get_driver():
        return webdriver.Chrome()
