from pages.base_page import BasePage
from locators.locators import MainPageLocators

class MainPage(BasePage):
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def click_personal_account_button(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor_link(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    def click_logo(self):
        self.click(MainPageLocators.LOGO)
