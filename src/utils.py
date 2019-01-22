"""
Different project related utilities like Selenium driver connection
"""
from typing import Union
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver import Remote
import psutil

from src.singleton.singleton_factory import SingletonFactory


def get_appium_driver(url, desired_capabilities) -> Remote:
    """
    Return the same instance to the Appium driver.

    :param url: the URL (address and port) where the service runs.
    :param desired_capabilities: session configuration data.
    :return: returns the SAME instance of the driver
    """
    return SingletonFactory.build(Remote,
                                  command_executor=url,
                                  desired_capabilities=desired_capabilities)


def get_selenium_driver(browser_name: str) -> Union[Chrome, Firefox]:
    """
    Return the same instance to the Selenium driver.

    :param browser_name: the name of the browser: chrome or mozilla
    :type browser_name: str
    :return: an instance of the required driver.
    :rtype: Union[Chrome, Mozilla]
    """
    if browser_name.upper() == 'CHROME':
        return SingletonFactory.build(Chrome)

    elif browser_name.upper() == 'Mozilla':
        return SingletonFactory.build(Firefox)

    else:
        raise NotImplementedError


def click_retry(driver: Union[Chrome, Firefox], element_identifier: str, id_type: str):
    """
    Click on elements based on id type.
    Currently supported ids are:
    * xpath
    * css_selector

    :param driver: browser Driver
    :type driver: object
    :param element_identifier: id of the element
    :type element_identifier: str
    :param id_type: selector type e.g. xpath
    :type id_type: str
    """

    def retry(action: staticmethod):
        """
        Retry an action if raise an error

        :param action: click to be performed
        :type action: staticmethod
        """
        try:
            action
        except RuntimeError:
            action

    if id_type == 'xpath':
        retry(driver.find_element_by_xpath(element_identifier).click())
    else:
        retry(driver.find_element_by_css_selector(element_identifier).click())


def get_process_info_spike(process):
    """

    :param process: get system information like memory consumption, cpu usage
    :return:
    """
    for process_id in psutil.pids():
        p = psutil.Process(process_id)
        if p.name() == 'pycharm':
            if process == 'memory':
                return p.memory_percent()
            elif process == 'cpu':
                return p.cpu_percent(interval=1)
            else:
                return p
