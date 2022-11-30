from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def alert_should_contain_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_add_to_basket_alert = self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD_TO_BASKET_ALERT).text
        assert product_name == product_name_in_add_to_basket_alert, f"Alert does not contain '{product_name}'."

    def basket_price_is_the_same_with_product_price(self):
        price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_add_to_basket_alert = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert price_on_page == price_in_add_to_basket_alert, "Product price and price in 'basket total' alert not the same."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared."
