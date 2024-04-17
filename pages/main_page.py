import time
from locators.locators import Construction as cp
from pages.base_pages import BasePage

class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def check_close_modal_window_ingredient(self):
        self.click_on_element(cp.first_ingredient)
        self.get_element_text(cp.check_text_details_ingredient)
        time.sleep(1)
        self.click_on_element(cp.close_ingredient_window)
        time.sleep(1)

    def get_first_count_ingredient(self):
        return self.find(cp.first_ingredient).text

