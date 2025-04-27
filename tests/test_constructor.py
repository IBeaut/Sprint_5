import pytest
from locators.locators import MainPageLocators
from pages.base_page import BasePage
import time

URL_MAIN = "https://stellarburgers.nomoreparties.site/"

def test_constructor_sections(driver):
    base_page = BasePage(driver)
    base_page.open(URL_MAIN)

    # Проверка перехода к "Соусам"
    sauce_button = driver.find_element_by_xpath("//span[text()='Соусы']")
    sauce_button.click()
    assert sauce_button.is_displayed()

    time.sleep(1)

    # Проверка перехода к "Начинкам"
    filling_button = driver.find_element_by_xpath("//span[text()='Начинки']")
    filling_button.click()
    assert filling_button.is_displayed()

    time.sleep(1)

    # Проверка перехода к "Булкам"
    bun_button = driver.find_element_by_xpath("//span[text()='Булки']")
    bun_button.click()
    assert bun_button.is_displayed()
