import pytest
from locators.locators import MainPageLocators, LoginPageLocators
from pages.base_page import BasePage
from utils.user_generator import generate_email, generate_password
from selenium.webdriver.common.by import By
import time

URL_MAIN = "https://stellarburgers.nomoreparties.site/"
URL_LOGIN = "https://stellarburgers.nomoreparties.site/login"
URL_REGISTER = "https://stellarburgers.nomoreparties.site/register"
URL_FORGOT_PASSWORD = "https://stellarburgers.nomoreparties.site/forgot-password"

@pytest.fixture
def registered_user(driver):
    # Регистрация нового пользователя перед тестами
    email = generate_email()
    password = "123456"  # простой валидный пароль
    driver.get(URL_REGISTER)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("TestUser")
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    # Даем сайту чуть подумать
    time.sleep(2)

    return email, password

def test_login_from_main_page(driver, registered_user):
    email, password = registered_user
    base_page = BasePage(driver)
    base_page.open(URL_MAIN)

    base_page.click(MainPageLocators.LOGIN_BUTTON)
    base_page.input_text(LoginPageLocators.EMAIL_INPUT, email)
    base_page.input_text(LoginPageLocators.PASSWORD_INPUT, password)
    base_page.click(LoginPageLocators.SUBMIT_BUTTON)

    assert base_page.is_element_visible(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

def test_login_from_personal_account_button(driver, registered_user):
    email, password = registered_user
    base_page = BasePage(driver)
    base_page.open(URL_MAIN)

    base_page.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    base_page.input_text(LoginPageLocators.EMAIL_INPUT, email)
    base_page.input_text(LoginPageLocators.PASSWORD_INPUT, password)
    base_page.click(LoginPageLocators.SUBMIT_BUTTON)

    assert base_page.is_element_visible(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

def test_login_from_register_form(driver, registered_user):
    email, password = registered_user
    base_page = BasePage(driver)
    base_page.open(URL_REGISTER)

    base_page.click(LoginPageLocators.REGISTRATION_LINK)
    base_page.input_text(LoginPageLocators.EMAIL_INPUT, email)
    base_page.input_text(LoginPageLocators.PASSWORD_INPUT, password)
    base_page.click(LoginPageLocators.SUBMIT_BUTTON)

    assert base_page.is_element_visible(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

def test_login_from_forgot_password_form(driver, registered_user):
    email, password = registered_user
    base_page = BasePage(driver)
    base_page.open(URL_FORGOT_PASSWORD)

    base_page.click(LoginPageLocators.FORGOT_PASSWORD_LINK)
    base_page.input_text(LoginPageLocators.EMAIL_INPUT, email)
    base_page.input_text(LoginPageLocators.PASSWORD_INPUT, password)
    base_page.click(LoginPageLocators.SUBMIT_BUTTON)

    assert base_page.is_element_visible(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
