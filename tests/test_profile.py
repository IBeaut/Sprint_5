import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from pages.base_page import BasePage

URL_MAIN = "https://stellarburgers.nomoreparties.site/"

def test_logout_from_profile(driver, logged_in_user):
    base_page = BasePage(driver)
    base_page.open(URL_MAIN)

    base_page.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON)
    )
    base_page.click(ProfilePageLocators.EXIT_BUTTON)

    assert base_page.is_element_visible(LoginPageLocators.SUBMIT_BUTTON)
