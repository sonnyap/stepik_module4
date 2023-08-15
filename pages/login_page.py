from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        expected_substring = "login"
        current_url = self.browser.current_url
        assert expected_substring in current_url, f"Подстрока '{expected_substring}' не найдена в текущем URL: {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_confirm_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

