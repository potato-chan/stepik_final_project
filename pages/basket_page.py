from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def text_empty_basket_is_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Text 'Empty basket' is not presented, but should be."

    def should_not_be_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products in the basket is presented, but should not be."
