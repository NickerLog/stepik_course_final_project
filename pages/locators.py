from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form[id="register_form"]')


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    INFO_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')

