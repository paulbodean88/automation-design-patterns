import time

from src.factory.factory_method import MenuAndSearchTest
from src.utils import get_selenium_driver


def test_sal():
    dr = get_selenium_driver('chrome')
    dr.set_window_size(1200, 800)
    dr.get('https://www.youtube.com/')

    demo = MenuAndSearchTest(dr)
    time.sleep(2.0)
    demo.get_sections()['menu'].get_actions('click_menu')
    demo.get_sections()['menu'].get_actions('trend')
    demo.get_sections()['menu'].get_actions('history')
    demo.get_sections()['search'].get_actions('set_query', 'Despacido')
    demo.get_sections()['search'].get_actions('click_search')
    dr.quit()
