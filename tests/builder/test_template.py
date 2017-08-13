from unittest import TestCase

from src.builder.template_test_case import TestTemplate
from src.utils import get_selenium_driver


class TestTestTemplate(TestCase):

    def setUp(self):
        driver = get_selenium_driver('chrome')
        driver.get('https://www.youtube.com/')
        self.template = TestTemplate(driver)

    def test_one(self):
        self.template.wait(1)
        self.template.click_element('//*[@id="appbar-guide-button"]/span/span')
        self.template.wait(1)
        self.template.execute_test()


