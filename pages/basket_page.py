from pages.base_page import BasePage
from pages.locators import BasketLocators

class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketLocators.BASKET_HEADER), "No Basket header presented"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET), "Basket empty check failed. No empty reasonlocator"
        assert self.is_not_element_present(*BasketLocators.NOT_EMPTY_BASKET), "Basket contains something"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketLocators.NOT_EMPTY_BASKET), "Basket empty check failed. No empty reasonlocator"
        assert self.is_not_element_present(*BasketLocators.EMPTY_BASKET), "Basket contains something"