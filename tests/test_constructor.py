import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorPageLocators

URL_MAIN = "https://stellarburgers.nomoreparties.site/"

def test_constructor_sections(driver):
    base_page = BasePage(driver)
    base_page.open(URL_MAIN)

    wait = WebDriverWait(driver, 5)

    # Проверка таба "Соусы"
    sauce_tab = wait.until(EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB))
    sauce_tab.click()
    active_sauce = wait.until(EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB("Соусы")))
    assert active_sauce.is_displayed()

    # Проверка таба "Начинки"
    fillings_tab = wait.until(EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB))
    fillings_tab.click()
    active_fillings = wait.until(EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB("Начинки")))
    assert active_fillings.is_displayed()

    # Проверка таба "Булки"
    buns_tab = wait.until(EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB))
    buns_tab.click()
    active_buns = wait.until(EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB("Булки")))
    assert active_buns.is_displayed()
