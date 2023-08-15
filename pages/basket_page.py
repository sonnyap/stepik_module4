from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty_message(self):
        assert self.get_text(
            BasketPageLocators.MESSAGE_EMPTY_BASKET) == "Your basket is empty. Continue shopping", "Basket is not empty"
