"""
Define a one to many relationship between objects.
If the state of an object is changed, all the others are notified
"""
from src.page_object_pattern.home_page import HomePage
from src.utils import get_selenium_driver, get_process_info_spike


class Process:
    """
     - is aware of observers
     - send a notification to the observers if its state is changed
    """

    def __init__(self):
        self._observers = set()

    def subscribe(self, who):
        self._observers.add(who)

    def un_subscribe(self, who):
        self._observers.discard(who)

    def dispatch(self,test_func, message):
        for subscriber in self._observers:
            if get_process_info_spike(message) >= 50:
                subscriber.update(test_func, 'CPU usage warning: ' + str(get_process_info_spike(message)))
            else:
                subscriber.update(test_func, 'CPU usage normal: ' + str(get_process_info_spike(message)))


class Tests:
    """
    Define the observant class
    """
    def __init__(self, name):
        self.name = name

    def update(self, test_func, message):
        test_func()
        print('{} test measurement - "{}"'.format(self.name, message))


def search_test():
    driver = get_selenium_driver('CHROME')
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    main_page = HomePage(driver)
    main_page.login()
    main_page.search()
    driver.quit()


if __name__ == '__main__':
    process = Process()
    test_search = Tests('Search')
    process.subscribe(test_search)
    process.dispatch(search_test, 'cpu')
