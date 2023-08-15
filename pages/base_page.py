from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector, element):
        try:
            self.browser.find_element(selector, element)
        except NoSuchElementException:
            raise AssertionError(f"Element {element} is not  present using {selector}")
        return True

    def wait_for_element_exist(self, selector, element, timeout=20):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((selector, element)))
        except TimeoutException:
            raise AssertionError(f"Element {element} not found using {selector}")
        return True

    def wait_for_element_clickable(self, selector, element, timeout=20):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((selector, element)))
        except TimeoutException:
            raise AssertionError(f"Element {element} not clickable using {selector}")
        return True

    def click(self, locator):
        self.wait_for_element_exist(*locator)
        assert self.wait_for_element_clickable(*locator), f"Element {locator} is not clickable"
        self.browser.find_element(*locator).click()

    def get_text(self, locator):
        self.wait_for_element_exist(*locator)
        return self.browser.find_element(*locator).text

    def is_not_element_present(self, selector, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((selector, element)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, selector, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((selector, element)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.is_element_present(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        self.click(BasePageLocators.BASKET_LINK)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
