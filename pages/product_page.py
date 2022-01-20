from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_promo_newyear_in_url(self):
        assert "?promo=newYear" in self.browser.current_url, "url doesn't have '?promo=newYear'"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), \
            'Cannot locate add-to-cart-button on page'

    def go_to_add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_information_message(self):
        assert self.is_element_present(*ProductPageLocators.INFO_MESSAGE), "not found info message about add-to-cart"

    def should_text_match_in_message(self):
        assert self.is_text_on_element_matching(*ProductPageLocators.PRODUCT_NAME, *ProductPageLocators.INFO_MESSAGE), \
            f"text on add-to-cart info massage doesn't match with Product name"

    def go_to_add_product_to_cart(self):
        self.should_be_add_to_cart_button()
        self.go_to_add_to_cart_button()
        self.should_be_information_message()
        self.should_text_match_in_message()
