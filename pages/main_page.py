from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def should_be_main_page(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_HEADER), "No 'Welcome!' header"