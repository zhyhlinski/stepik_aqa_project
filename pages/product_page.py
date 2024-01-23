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

    def item_name_check_in_alert_message(self):
        assert self.get_item_name() == self.get_item_name_from_alert(), "Item name check failed"

    def price_check_in_alert_message(self):
        assert self.get_item_price() == self.get_price_from_alert(), "Price check failed"

    def should_be_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE_LOCATOR), "No product page locator"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_NAME_ADDED_TO_BASKET_ALERT), \
           "Success message isn't disappeared"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_NAME_ADDED_TO_BASKET_ALERT), \
           "Success message is presented, but should not be"
