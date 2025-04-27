from pages.base_page import BasePage
from locators.locators import LoginPageLocators

class LoginPage(BasePage):
    def input_email(self, email):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    def input_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    def go_to_register_page(self):
        self.click(LoginPageLocators.REGISTRATION_LINK)

    def go_to_forgot_password_page(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)
