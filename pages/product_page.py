from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_basket(self):
        button = self.get_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_item_name(self):
        return self.get_element(*ProductPageLocators.ITEM_NAME).text

    def get_item_price(self):
        return self.get_element(*ProductPageLocators.ITEM_PRICE).text

    def get_price_from_alert(self):
        return self.get_element(*ProductPageLocators.ITEM_PRICE_ADDED_TO_BASKET).text

    def get_item_name_from_alert(self):
        return self.get_element(*ProductPageLocators.ITEM_NAME_ADDED_TO_BASKET_ALERT).text

