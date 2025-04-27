import pytest
from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from pages.base_page import BasePage
from utils.user_generator import generate_email, generate_password
import time

URL_MAIN = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture
def logged_in_user(driver):
    # Регистрируем и логиним пользователя
    email = generate_email()
    password = "123456"
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element_by_name('name').send_keys("TestUser")
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('Пароль').send_keys(password)
    driver.find_element_by_xpath("//button[text()='Зарегистрироваться']").click()
    time.sleep(2)

    driver.get(URL_MAIN)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
    time.sleep(2)

    return email, password

def test_logout_from_profile(driver, logged_in_user):
    base_page = BasePage(driver)
    base_page.open(URL_MAIN)

    base_page.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    time.sleep(1)
    base_page.click(ProfilePageLocators.EXIT_BUTTON)

    assert base_page.is_element_visible(LoginPageLocators.SUBMIT_BUTTON)
