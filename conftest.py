import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.user_generator import generate_email
from locators.locators import MainPageLocators, LoginPageLocators

@pytest.fixture
def logged_in_user(driver):
    email = generate_email()
    password = "123456"
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.NAME, 'name').send_keys("TestUser")
    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'Пароль').send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 5).until(EC.url_contains("login"))

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_matches("https://stellarburgers.nomoreparties.site/"))

    return email, password
