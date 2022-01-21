from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_anything_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ALL_ELEMENTS_IN), \
            "product is located in basket, but not should be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_IN_EMPTY_BASKET), \
            "doesn't located message about empty basket"

