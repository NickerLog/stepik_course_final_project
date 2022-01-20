from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_text_on_element_matching(self, how_search_text_element, what_text_element,
                                    how_search_with_text_element, what_with_text_element):
        if (self.browser.find_element(how_search_text_element, what_text_element)).text in \
                (self.browser.find_element(how_search_with_text_element, what_with_text_element)).text:
            return True
        else:
            return False
