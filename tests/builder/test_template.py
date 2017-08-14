from unittest import TestCase

from src.builder.template_test_case import TemplateTestBuilder
from src.utils import get_selenium_driver


class TestTemplateTestBuilder(TestCase):

    def setUp(self):
        self.driver = get_selenium_driver('chrome')
        self.driver.get('https://www.youtube.com/')

    def test_one(self):
        test_case = TemplateTestBuilder(self.driver)\
                     .wait(1) \
                     .click_element('//*[@id="appbar-guide-button"]/span/span') \
                     .wait(1) \
                     .build()

        test_case.execute()
