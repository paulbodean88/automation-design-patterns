"""
Description:
    - Check the object instance memory location

@author: Paul Bodean
@date: 26/12/2017
"""
from unittest import TestCase

from src.singleton.singleton_metaclass import Driver


class TestMetaSingleton(TestCase):
    def test_singleton(self):
        dr1 = Driver().connect()
        dr2 = Driver().connect()

        self.assertEqual(dr1, dr2)
