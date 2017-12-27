"""
Description: module providing the implementation of the search class of the object pattern pattern
class declaration.

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.base_page import BasePage


class SearchPage(BasePage):
    """
    Search page
    """
    HEADING = 'firstHeading'
    SEE_ALSO = 'See_also'
    DOMAIN_ARTICLES = 'Domain-specific_articles'
    READING = 'Further_reading'
    REF = 'References'
    EXTERNAL_LINKS = 'External_links'

    def heading_text(self):
        """
        :return: Get the heading text
        """
        return self._driver.find_element_by_id(SearchPage.HEADING).text

    def see_also_text(self):
        """
        :return: see also text
        """
        return self._driver.find_element_by_xpath(SearchPage.SEE_ALSO).text

    def domain_articles_text(self):
        """
        :return: domain article title
        """
        return self._driver.find_element_by_xpath(SearchPage.DOMAIN_ARTICLES).text

    def reading_text(self):
        """
        :return: reading text
        """
        return self._driver.find_element_by_xpath(SearchPage.READING).text

    def ref_text(self):
        """
        :return: reference text value
        """
        return self._driver.find_element_by_xpath(SearchPage.REF).text

    def external_links_text(self):
        """
        :return: external links text value
        """
        return self._driver.find_element_by_xpath(SearchPage.EXTERNAL_LINKS).text
