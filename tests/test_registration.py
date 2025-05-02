# tests/test_registration.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import TestLocators

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    register_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_register))
    driver.execute_script("arguments[0].click();", register_button)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_name)).send_keys("Test User")
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_email)).send_keys("testtestov1999@yandex.ru")
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_password)).send_keys("password")
    submit_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_submit))
    driver.execute_script("arguments[0].click();", submit_button)
    assert WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text == "Соберите бургер"

def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    register_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_register))
    driver.execute_script("arguments[0].click();", register_button)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_name)).send_keys("Test User")
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_email)).send_keys("testtestov1999@yandex.ru")
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.input_password)).send_keys("pass")
    submit_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_submit))
    driver.execute_script("arguments[0].click();", submit_button)
    assert WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']"))).text == "Некорректный пароль"