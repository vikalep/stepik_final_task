from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.NAME, "login_submit")
    LOGIN_RESET_PASS_LINK = (By.LINK_TEXT, "I've forgotten my password")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'col-sm-6 product_main')]/h1")
    MSG_PRODUCT_ADD_TO_BASKET = (By.XPATH, "//div[contains(@class, 'alertinner')]/strong")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'col-sm-6 product_main')]/p")
    MSG_PRICE_IN_BASKET = (By.XPATH, "//div[contains(@class, 'alertinner')]/p/strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_VIEW_BASKET = (By.XPATH, "//a[@class = 'btn btn-default']")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
    