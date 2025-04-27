class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()
