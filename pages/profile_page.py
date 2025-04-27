from pages.base_page import BasePage
from locators.locators import ProfilePageLocators

class ProfilePage(BasePage):
    def click_exit_button(self):
        self.click(ProfilePageLocators.EXIT_BUTTON)
