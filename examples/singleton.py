"""

"""
from src.singleton.simple_singleton import MyClassBuilder
from src.singleton.singleton_factory import SingletonFactory


class A(object):

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'A' + str(self.__name)


class B(object):

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'B' + str(self.__name)


if __name__ == '__main__':

    # emphasize the singleton factory
    a = SingletonFactory.build(A, name='class A')
    aa = SingletonFactory.build(A)

    print('id for class instance a', id(a))
    print('id for class instance aa', id(aa))

    b = SingletonFactory.build(B, name='class B')
    bb = SingletonFactory.build(B)

    print('id for class instance b', id(b))
    print('id for class instance bb', id(bb))

    # emphasize the simple singleton
    my_class = MyClassBuilder.build(name='my class')
    my_class2 = MyClassBuilder.build(name='my class')

    print('id for class instance my_class', id(b))
    print('id for class instance my_class2', id(bb))
