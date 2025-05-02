# tests/test_login.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import TestLocators

def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    login_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_login_in_main))
    driver.execute_script("arguments[0].click();", login_button)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_email_auth)).send_keys("testtestov1999@yandex.ru")
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_password_auth)).send_keys("password")
    login_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_login))
    driver.execute_script("arguments[0].click();", login_button)
    assert WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text == "Соберите бургер"

def test_login_from_personal_cabinet(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    personal_cabinet_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_personal_account))
    driver.execute_script("arguments[0].click();", personal_cabinet_button)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_email_auth)).send_keys("testtestov1999@yandex.ru")
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_password_auth)).send_keys("password")
    login_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_login))
    driver.execute_script("arguments[0].click();", login_button)
    assert WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text == "Соберите бургер"