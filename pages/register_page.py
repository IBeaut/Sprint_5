from pages.base_page import BasePage
from locators.locators import RegisterPageLocators

class RegisterPage(BasePage):
    def input_name(self, name):
        self.input_text(RegisterPageLocators.NAME_INPUT, name)

    def input_email(self, email):
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)

    def input_password(self, password):
        self.input_text(RegisterPageLocators.PASSWORD_INPUT, password)

    def click_register_button(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    def get_error_message(self):
        return self.get_element(RegisterPageLocators.ERROR_MESSAGE).text
