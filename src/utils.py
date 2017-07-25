"""
Different project related utilities like Selenium driver connection
"""
from typing import Union
from webbrowser import Chrome, Mozilla

from selenium.webdriver import Remote

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


def get_selenium_driver(browser_name: str) -> Union[Chrome, Mozilla]:
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
        return SingletonFactory.build(Mozilla)

    else:
        raise NotImplementedError

