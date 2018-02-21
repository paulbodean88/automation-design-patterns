import abc


class TestManager:
    """
    Control the construction process, having a builder associated with it
    It delegates to the builder the implementation details,
    and deliver the already implemented functionality to the client
    """

    __builder = None

    def set_manager(self, builder):
        self.__builder = builder

    def get_test(self):
        # test = Test()
        # Pre validation
        pre_validation = self.__builder.get_pre_validation()
        print(pre_validation)
        # test.set_pre_validation(pre_validation)
        # Set wait
        wait = self.__builder.get_wait()
        print(wait)
        # test.set_wait(wait)
        # Set action
        action = self.__builder.get_actions()
        print(action)
        # test.set_action(action)
        # Make comparison
        comparison = self.__builder.get_post_validation()
        print(comparison)
        # test.set_post_validation(comparison)
        # Post results
        report = self.__builder.get_report()
        print(report)
        # test.set_report(report)


class Test:
    """
    Represent the complex object under construction.
    """

    def __init__(self):
        pass
        # self._pre_validation = None
        # self._wait = None
        # self._action = None
        # self._post_validation = None
        # self._report = None

    # def set_pre_validation(self, action):
    #     self._pre_validation = action
    #
    # def set_wait(self, action):
    #     self._wait = action
    #
    # def set_action(self, action):
    #     self._action = action
    #
    # def set_post_validation(self, action):
    #     self._post_validation = action
    #
    # def set_report(self, action):
    #     self._report = action


class Builder(metaclass=abc.ABCMeta):
    """
    Abstract interface for defining parts of the Product
    """

    def __init__(self):
        self.product = Test()

    @abc.abstractmethod
    def get_pre_validation(self):
        pass

    @abc.abstractmethod
    def get_wait(self):
        pass

    @abc.abstractmethod
    def get_actions(self):
        pass

    @abc.abstractmethod
    def get_post_validation(self):
        pass

    @abc.abstractmethod
    def get_report(self):
        pass


class HomePage(Builder):
    def get_pre_validation(self):
        return "pre_validation"

    def get_actions(self):
        return "actions"

    def get_wait(self):
        return "wait"

    def get_post_validation(self):
        return "post_validation"

    def get_report(self):
        return "report"


class SearchPage(Builder):
    def get_pre_validation(self):
        pass

    def get_actions(self):
        pass

    def get_wait(self):
        pass

    def get_post_validation(self):
        pass

    def get_report(self):
        pass


home_builder = HomePage()
manager = TestManager()
manager.set_manager(home_builder)
manager.get_test()

# print('home_test', home_test.set_report("demo"))
