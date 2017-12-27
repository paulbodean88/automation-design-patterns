from src.page_object_pattern.home_page import HomePage


class test_main():
    def test_bat(self):
        driver = HomePage()
        driver.open("https://en.wikipedia.org/wiki/Main_Page")
        driver.set_full_screen()
        driver.set_search_query("Design patterns")
        driver.search()
        driver.quit_browser()


demo = test_main()
demo.test_bat()
