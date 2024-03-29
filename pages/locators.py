from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form[id="register_form"]')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, 'input#id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    SUCCESS_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner.wicon')


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    INFO_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOOK_AT_CART_BUTTON = (By.CSS_SELECTOR, '.btn-group>.btn-default')
    USER_ICON = (By.CSS_SELECTOR, 'i.icon-user')


class BasketPageLocators:
    BASKET_ALL_ELEMENTS_IN = (By.CSS_SELECTOR, 'form.basket_summary>.basket-items')
    TEXT_IN_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')


