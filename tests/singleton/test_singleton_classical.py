"""
Description:
    - Check the object instance memory location

@author: Paul Bodean
@date: 26/12/2017
"""
from unittest import TestCase

from src.singleton.singleton_classical import ClassicalSingleton


class TestSingleton(TestCase):
    def test_singleton(self):
        s = ClassicalSingleton()
        d = ClassicalSingleton()
        self.assertEqual(s, d)
