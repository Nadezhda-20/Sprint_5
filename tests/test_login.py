import pytest
from conftest import generate_email, generate_password, generate_name, wait_for_element, wait_for_clickable, is_element_displayed
from locators import *


class TestLogin:
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

    def test_login_via_main_page_button(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной."""
        # Регистрируем пользователя
        email, password = self.register_user(driver)
        
        # Логинимся через кнопку "Войти в аккаунт" на главной
        driver.get("https://stellarburgers.education-services.ru")
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Проверяем, что вошли в аккаунт
        assert is_element_displayed(driver, ORDER_BUTTON)

    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку «Личный кабинет»."""
        # Регистрируем пользователя
        email, password = self.register_user(driver)
        
        # Логинимся через кнопку "Личный кабинет"
        driver.get("https://stellarburgers.education-services.ru")
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Проверяем, что вошли в аккаунт
        assert is_element_displayed(driver, ORDER_BUTTON)

    def test_login_via_registration_form(self, driver):
        """Вход через кнопку в форме регистрации."""
        # Регистрируем пользователя
        email, password = self.register_user(driver)
        
        # Логинимся через кнопку в форме регистрации
        driver.get("https://stellarburgers.education-services.ru")
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        wait_for_clickable(driver, REGISTER_LINK).click()
        wait_for_clickable(driver, LOGIN_LINK_FROM_REGISTER).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Проверяем, что вошли в аккаунт
        assert is_element_displayed(driver, ORDER_BUTTON)

    def test_login_via_password_recovery_form(self, driver):
        """Вход через кнопку в форме восстановления пароля."""
        # Регистрируем пользователя
        email, password = self.register_user(driver)
        
        # Логинимся через кнопку в форме восстановления пароля
        driver.get("https://stellarburgers.education-services.ru")
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        wait_for_clickable(driver, RECOVER_PASSWORD_LINK).click()
        wait_for_clickable(driver, LOGIN_LINK_FROM_RECOVER).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Проверяем, что вошли в аккаунт
        assert is_element_displayed(driver, ORDER_BUTTON)
