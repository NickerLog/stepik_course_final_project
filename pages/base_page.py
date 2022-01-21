from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_present_with_wait(self, how, what, timeout):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_text_on_element_matching(self, how_search_text_element, what_text_element,
                                    how_search_with_text_element, what_with_text_element):
        if (self.browser.find_element(how_search_text_element, what_text_element)).text == \
                (self.browser.find_element(how_search_with_text_element, what_with_text_element)).text:
            return True
        else:
            return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'login link is not presented'

    def go_to_cart(self):
        go_to_cart_button = self.browser.find_element(*BasePageLocators.LOOK_AT_CART_BUTTON)
        go_to_cart_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
