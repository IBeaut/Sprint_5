from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")

    ACTIVE_TAB = lambda text: (By.XPATH, f"//div[contains(@class, 'tab_tab_type_current')]/span[text()='{text}']")
