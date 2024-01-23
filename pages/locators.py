from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_HEADER = (By.CSS_SELECTOR, "div.page-header.action h1")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    SUBMIT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WELCOME_HEADER = (By.CSS_SELECTOR, "section.well div h2")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ITEM_NAME_ADDED_TO_BASKET_ALERT = (By.CSS_SELECTOR, "#messages div div strong")
    ITEM_PRICE_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alert-info div.alertinner p strong")
    PRODUCT_PAGE_LOCATOR = (By.CSS_SELECTOR, "article.product_page")
