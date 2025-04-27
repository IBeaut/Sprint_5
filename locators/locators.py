from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка входа на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка "Личный кабинет"
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # Ссылка на конструктор
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип Stellar Burgers

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name") # Поле email
    PASSWORD_INPUT = (By.NAME, "Пароль") # Поле пароль
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка входа
    REGISTRATION_LINK = (By.LINK_TEXT, "Зарегистрироваться") # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль") # Ссылка на восстановление пароля

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']") # Поле имя
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']") # Поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']") # Поле пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка зарегистрироваться
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error") # Сообщение об ошибке

class ProfilePageLocators:
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка выхода
