"""
Description: Module that describes the pythonic way to implement the singleton design pattern over
class declaration.

@author: Eugen
@date: 24/07/2017
"""


class MyClassBuilder(object):
    """
    Wrapper class for the actual class which implements the singleton design pattern.
    """

    class __PrivateMyClass(object):
        """
        Actual implementation of the class.
        Together with all the methods and attributes.
        """

        def __init__(self, name):
            """
            Constructor with arguments.
            :param name: an attribute for the class.
            """

            self.__name = name

        def __str__(self):
            """
            ToString method for the class.
            :return: returns a string with the state of the class instance.
            """

            return str(self.__name)

    __instance = None

    @staticmethod
    def build(**constructor_args):
        """
        Builder for the class.
        The ONLY EXPOSED way to create an instance of the class __PrivateMyClass.
        
        Creates a private instance of the actual class and returns it. Else if the class is already
        instantiated, it returns the initial instance of the class.
        :param constructor_args: the constructor arguments for the class.
        :return: returns the instance of the class __PrivateMyClass
        """

        # if the class has not yet been instantiated, create it
        if MyClassBuilder.__instance is None:
            MyClassBuilder.__instance = MyClassBuilder.__PrivateMyClass(**constructor_args)

        return MyClassBuilder.__instance
