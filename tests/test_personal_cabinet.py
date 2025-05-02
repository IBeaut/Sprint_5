# tests/test_personal_cabinet.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import TestLocators

def test_transition_to_personal_cabinet(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    personal_cabinet_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_personal_account))
    driver.execute_script("arguments[0].click();", personal_cabinet_button)
    assert WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Профиль']"))).text == "Профиль"

def test_transition_from_personal_cabinet_to_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    personal_cabinet_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.button_personal_account))
    driver.execute_script("arguments[0].click();", personal_cabinet_button)
    constructor_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.header_of_page_constructor))
    driver.execute_script("arguments[0].click();", constructor_button)
    assert WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text == "Соберите бургер"