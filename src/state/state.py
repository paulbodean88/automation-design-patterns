"""
This pattern provides different behaviours based on the internal object state
An implementation examples based on the test execution life cycle will be provided
"""
import abc

from src.utils import get_selenium_driver


class Manager:
    """
    State machine manager.
    Acting as an interface to the client and providing the actual state of the object
    """

    def __init__(self, state):
        """

        :param state: current object state
        """
        self._state = state

    def get_state(self):
        """

        :return: state getter
        """
        self._state.run()


class State(metaclass=abc.ABCMeta):
    """
    Interface definition for behaviour encapsulation
    """

    def __init__(self):
        self._driver = get_selenium_driver('chrome')

    def get_driver(self):
        return self._driver

    @abc.abstractmethod
    def run(self):
        pass


class StartTest(State):
    """
    Prepare the test execution environment
    """

    def run(self):
        print(" Start test state!!! ")
        self.get_driver().get('https://en.wikipedia.org/')


class ExecuteTest(State):
    """
    Run run different test steps
    """

    SEARCH_BUTTON = 'searchButton'

    def run(self):
        print(" Execute test steps state!!! ")
        if self.get_driver().find_element_by_id(ExecuteTest.SEARCH_BUTTON).is_displayed():
            print("Search button available")
            self._driver.find_element_by_id(ExecuteTest.SEARCH_BUTTON).click()
        else:
            print("Search button not available")


class StopTest(State):
    """
    Close the testing session
    """

    def run(self):
        print(" Stop test state!!! ")
        self.get_driver().quit()


if __name__ == '__main__':
    start = StartTest()
    execute = ExecuteTest()
    stop = StopTest()
    for test_state in [start, execute, stop]:
        manager = Manager(test_state)
        manager.get_state()
