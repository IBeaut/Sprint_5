import pytest
from locators.locators import MainPageLocators, RegisterPageLocators
from pages.base_page import BasePage
from utils.user_generator import generate_email, generate_password

URL = "https://stellarburgers.nomoreparties.site/register"


def test_successful_registration(driver):
    base_page = BasePage(driver)
    base_page.open(URL)

    email = generate_email()
    password = generate_password()

    base_page.input_text(RegisterPageLocators.NAME_INPUT, "TestUser")
    base_page.input_text(RegisterPageLocators.EMAIL_INPUT, email)
    base_page.input_text(RegisterPageLocators.PASSWORD_INPUT, password)
    base_page.click(RegisterPageLocators.REGISTER_BUTTON)

    # После регистрации перекидывает на страницу логина
    assert base_page.is_element_visible(LoginPageLocators.SUBMIT_BUTTON)
