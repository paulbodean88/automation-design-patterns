"""
Description: Test module for module src/singleton/simple_singleton.py

@author: Eugen
@date: 24/07/2017
"""

from unittest import TestCase

from src.singleton.simple_singleton import MyClassBuilder


class TestMyClassBuilder(TestCase):
    def test_build(self):
        my_class = MyClassBuilder.build(name='my class')
        my_class2 = MyClassBuilder.build()
        my_class3 = MyClassBuilder.build(name='my class 2')

        self.assertEqual(str(id(my_class)), str(id(my_class2)))
        self.assertEqual(str(my_class3), 'my class')
