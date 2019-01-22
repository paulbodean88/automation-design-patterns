"""
Description:
    - Check Driver connection following both singleton approaches

@author: Paul Bodean
@date: 26/12/2017
"""
from unittest import TestCase
from src.singleton.singleton_decor import MyDriver, Driver


class TestDecoratorSingleton(TestCase):
    def test_singleton(self):
        dr1 = Driver()
        dr1.get_driver().get('https://en.wikipedia.org/')
        dr2 = Driver()

        self.assertEqual(dr1, dr2)

    def test_my_singleton(self):
        dr1 = MyDriver()
        dr1.get_driver().get('https://en.wikipedia.org/')
        dr2 = MyDriver()

        self.assertEqual(dr1, dr2)
