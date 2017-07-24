"""
Description: 

@author: Eugen
@date: 24/07/2017
"""
from unittest import TestCase

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


class TestSingletonFactory(TestCase):
    def test_build(self):
        a = SingletonFactory.build(A, name='class A')
        aa = SingletonFactory.build(A)

        self.assertEqual(str(id(a)), str(id(aa)))
        self.assertEqual(str(a), str(aa))

        b = SingletonFactory.build(B, name='class B')
        bb = SingletonFactory.build(B)

        self.assertEqual(str(id(b)), str(id(bb)))
        self.assertEqual(str(b), str(bb))

