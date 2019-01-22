"""
Description: Singleton implementation based on a metaclass

@author: Paul Bodean
@date: 23.01.2018
"""
from selenium import webdriver


class MetaClassSingleton(type):
    """
    Meta class implementation
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override __call__ special method based on singleton pattern
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Driver(metaclass=MetaClassSingleton):
    """
    Driver class decorated by the meta class: MetaClassSingleton.
    Behaviour changed in singleton
    """
    connection = None

    def connect(self):
        """
        Set the connection with the web driver
        :return: web driver
        """
        if self.connection is None:
            self.connection = webdriver.Chrome()

        return self.connection


# When we want to perform different interaction with a view, the driver class can be instantiated
# for multiple times, but only one object is created
dr1 = Driver().connect()
dr2 = Driver().connect()

print('Web driver object 1 ', dr1)
print('Web driver object 2', dr2)
