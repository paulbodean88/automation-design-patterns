"""
Description: Singleton implementation in python based on the lazy instantiation concept

@author: Paul Bodean
@date: 23.01.2018
"""
from selenium import webdriver


class LazyInstSingleton:
    __instance = None

    def __init__(self):
        if LazyInstSingleton.__instance is None:
            print('__init__ method called')
        else:
            raise ValueError("An instantiation already exists!", self.get_instance())
        webdriver.Chrome()

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = LazyInstSingleton()
        return cls.__instance


# Below we will execute the instantiation
s = LazyInstSingleton()  # class initialization
print("Obj created", LazyInstSingleton.get_instance())  # Object creation
d = LazyInstSingleton() # initialize again the class, so error will be raised
