"""
Different project related utilities like Selenium driver connection
"""

from selenium.webdriver import Remote

from src.singleton.singleton_factory import SingletonFactory


def get_driver(url, desired_capabilities):
    """
    Return the same instance to the Appium/Selenium driver.
    :param url: the URL (address and port) where the service runs.
    :param desired_capabilities: session configuration data.
    :return: returns the SAME instance of the driver
    """
    return SingletonFactory.build(Remote,
                                  command_executor=url,
                                  desired_capabilities=desired_capabilities)
