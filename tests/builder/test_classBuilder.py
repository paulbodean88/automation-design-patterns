from unittest import TestCase

from src.builder.builder import ClassBuilder


class TestClassBuilder(TestCase):

    def setUp(self):
        self.__class_builder = ClassBuilder('John', 30.0)

    def test_set_address(self):
        my_class = self.__class_builder.set_address('Cluj').build()
        self.assertEqual(my_class.address, 'Cluj')

    def test_set_color(self):
        my_class = self.__class_builder.set_color('Red').build()
        self.assertEqual(my_class.color, 'Red')

    def test_build(self):
        my_class = self.__class_builder.set_address('address').set_color('red').build()
        self.assertEqual(my_class.address, 'address')
        self.assertEqual(my_class.color, 'red')
