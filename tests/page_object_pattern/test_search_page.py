"""
Description: Test case implementation based on page object pattern and unittest

"""
from src.page_object_pattern.home_page import HomePage
from src.page_object_pattern.search_page import SearchPage
from src.page_object_pattern.test_template import TestTemplate


class TestSearchPage(TestTemplate):
    """
    Test class for testing a search on Youtube
    """

    def test_result_found(self):
        """
        Perform searches
        """
        home_page = HomePage(self.driver)
        home_page.set_search_query("Design patterns")
        home_page.search()
        result = SearchPage(self.driver)
        assert result.heading_text() == "Design pattern"
