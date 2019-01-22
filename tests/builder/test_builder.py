"""
Description: Test case implementation based on builder pattern and unittest

"""
from src.builder.builder import SearchFlow, TestManager
from src.page_object_pattern.test_template import TestTemplate


class TestSearchFlow(TestTemplate):
    """
    Test class for testing a search on Wikipedia
    """

    def test_flow(self):
        """
        Test Steps
        """
        home_builder = SearchFlow()
        manager = TestManager()
        manager.set_manager(home_builder)
        manager.get_test()
