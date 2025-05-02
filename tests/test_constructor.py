# tests/test_constructor.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators import TestLocators

def test_transition_to_constructor_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.header_of_page_constructor)).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text == "Соберите бургер"

def test_transition_to_constructor_from_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.button_personal_account)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.logo)).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text == "Соберите бургер"

def test_transition_to_buns_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    buns_section = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.buns_block))
    driver.execute_script("arguments[0].click();", buns_section)
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))).text == "Булки"