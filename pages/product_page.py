import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
	def add_product_to_buscket(self):
		btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
		btn_add_to_basket.click()

	def should_be_message_that_product_add_to_basket(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		msg_product_name = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_ADD_TO_BASKET).text
		assert product_name == msg_product_name, "Product name in mssg not matched with product name which add to cart"

	def should_be_right_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		msg_price_in_basket = self.browser.find_element(*ProductPageLocators.MSG_PRICE_IN_BASKET).text
		assert product_price == msg_price_in_basket, "Price in mssg not matched with product price which add to cart"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.MSG_PRODUCT_ADD_TO_BASKET), "Success message is presented, but should not be"
