"""
Description: Module that describes the pythonic way to implement the singleton design pattern
in order to work with a set of classes.

@author: Eugen
@date: 24/07/2017
"""


class SingletonFactory(object):
    """
    A factory of the same instances of injected classes.
    """

    # a mapping between the name of a class and the instance.
    __mappings = {}

    @staticmethod
    def build(class_, **constructor_args):
        """
        Builds an instance of the given class pointer together with the provided constructor arguments.
        Returns the SAME instance for a given class.
        
        :param class_: A pointer to the definition of the class. 
        :param constructor_args: The arguments for the class instance.
        :return: An instance of the provided class.
        """

        # if the class instance is mapped, then retrieve it.
        if str(class_) in SingletonFactory.__mappings:
            instance_ = SingletonFactory.__mappings[str(class_)]

        # else create the instance and map it to the class name.
        else:
            instance_ = class_(**constructor_args)
            SingletonFactory.__mappings[str(class_)] = instance_

        return instance_
