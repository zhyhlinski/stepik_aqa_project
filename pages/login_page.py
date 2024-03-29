from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.get_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.get_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON).click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)