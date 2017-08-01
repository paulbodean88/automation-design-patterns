"""

"""


class ClassBuilder(object):
    class __PrivateMyClass(object):
        """

        """

        def __init__(self, name: str, price: float):
            self.__name = name
            self.__price = price
            self.__address = 'undefined'
            self.__color = 'undefined'

        @property
        def address(self):
            return self.__address

        @address.setter
        def address(self, new_address):
            self.__address = new_address

        @property
        def color(self):
            return self.__color

        @color.setter
        def color(self, new_color):
            self.__color = new_color

        def __str__(self):
            return self.__name + ':' + str(self.__price) + ':' + self.__address + ':' + self.__color

    def __init__(self, name, price):
        self.__class = ClassBuilder.__PrivateMyClass(name, price)

    def set_address(self, address):
        self.__class.address = address
        return self

    def set_color(self, color):
        self.__class.color = color
        return self

    def build(self):
        return self.__class
