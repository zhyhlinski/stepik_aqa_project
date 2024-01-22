from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 10


def test_check_add_to_basket_form_presence(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)

    add_to_basket_button = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.ID,
                                                                                                 "add_to_basket_form")))
