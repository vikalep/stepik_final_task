from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "It's not a login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Log In form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_registered_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not registered, but should"
