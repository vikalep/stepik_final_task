from .base_page import BasePage
from .locators import BasePageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def go_to_view_basket(self):
        view_btn = self.browser.find_element(*BasePageLocators.BTN_VIEW_BASKET)
        view_btn.click()

    def should_be_empty_basket(self):
        empty_basket = self.browser.find_element(*BasePageLocators.EMPTY_BASKET).text
        assert "Your basket is empty. Continue shopping" == empty_basket, "Basket is not empty, but should be"

    def items_shouldnt_be_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_IN_BASKET), "Items in basket are presented, but should not be"
