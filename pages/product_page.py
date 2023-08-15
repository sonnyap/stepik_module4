import math

from selenium.common import NoAlertPresentException

from . import base_page
from .locators import ProductPageLocators


class ProductPage(base_page.BasePage):
    def add_to_basket(self):
        self.click(ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def compare_product_name(self):
        product_name = self.get_text(ProductPageLocators.PRODUCT_NAME)
        product_name_in_basket = self.get_text(ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name == product_name_in_basket, "Product name is not equal to product name in basket"

    def compare_product_price(self):
        product_price = self.get_text(ProductPageLocators.PRODUCT_PRICE)
        product_price_in_basket = self.get_text(ProductPageLocators.ALERT_PRODUCT_PRICE)
        assert product_price == product_price_in_basket, "Product price is not equal to product price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"

