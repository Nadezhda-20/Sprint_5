import pytest
from conftest import generate_email, generate_password, generate_name, wait_for_element, wait_for_clickable, is_element_displayed
from locators import *


class TestProfile:
    def register_user(self, driver):
        """Регистрирует нового пользователя и возвращает данные"""
        email = generate_email()
        password = generate_password(8)
        name = generate_name()
        
        # Регистрируем пользователя
        driver.get("https://stellarburgers.education-services.ru")
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        wait_for_clickable(driver, REGISTER_LINK).click()
        
        wait_for_element(driver, NAME_INPUT_REGISTER).send_keys(name)
        wait_for_element(driver, EMAIL_INPUT_REGISTER).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_REGISTER).send_keys(password)
        wait_for_clickable(driver, REGISTER_BUTTON).click()
        
        # Ждем перехода на страницу логина
        wait_for_element(driver, HEADER_LOGIN)
        
        return email, password

    def login_user(self, driver, email, password):
        """Логинит пользователя"""
        driver.get("https://stellarburgers.education-services.ru")
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Ждем загрузки главной страницы после логина
        wait_for_element(driver, HEADER_MAIN)

    def test_navigate_to_personal_account(self, driver):
        """Проверь переход по клику на «Личный кабинет»."""
        # Регистрируем и логиним пользователя
        email, password = self.register_user(driver)
        self.login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем, что перешли в личный кабинет
        assert is_element_displayed(driver, PROFILE_LINK)

    def test_navigate_from_profile_to_constructor_via_constructor_button(self, driver):
        """Проверь переход по клику на «Конструктор» из личного кабинета."""
        # Регистрируем и логиним пользователя
        email, password = self.register_user(driver)
        self.login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Переходим обратно в конструктор через кнопку "Конструктор"
        wait_for_clickable(driver, CONSTRUCTOR_BUTTON).click()
        
        # Проверяем, что вернулись на главную страницу конструктора
        assert is_element_displayed(driver, HEADER_MAIN)

    def test_navigate_from_profile_to_constructor_via_logo(self, driver):
        """Проверь переход по клику на логотип Stellar Burgers из личного кабинета."""
        # Регистрируем и логиним пользователя
        email, password = self.register_user(driver)
        self.login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Переходим обратно в конструктор через логотип
        wait_for_clickable(driver, LOGO_BUTTON).click()
        
        # Проверяем, что вернулись на главную страницу конструктора
        assert is_element_displayed(driver, HEADER_MAIN)

    def test_logout_from_account(self, driver):
        """Проверь выход по кнопке «Выйти» в личном кабинете."""
        # Регистрируем и логиним пользователя
        email, password = self.register_user(driver)
        self.login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Выходим из аккаунта
        wait_for_clickable(driver, LOGOUT_BUTTON).click()
        
        # Проверяем, что вышли из аккаунта (вернулись на страницу логина)
        assert is_element_displayed(driver, HEADER_LOGIN)
