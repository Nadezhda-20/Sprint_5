import pytest
from helpers import register_user, wait_for_element, wait_for_clickable, is_element_displayed
from locators import *
from urls import MAIN_PAGE_URL


class TestLogin:
    def test_login_via_main_page_button(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной."""
        # Регистрируем пользователя
        email, password = register_user(driver)
        
        # Логинимся через кнопку "Войти в аккаунт" на главной
        driver.get(MAIN_PAGE_URL)
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Проверяем, что вошли в аккаунт
        assert is_element_displayed(driver, ORDER_BUTTON)

    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку «Личный кабинет»."""
        # Регистрируем пользователя
        email, password = register_user(driver)
        
        # Логинимся через кнопку "Личный кабинет"
        driver.get(MAIN_PAGE_URL)
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Проверяем, что вошли в аккаунт
        assert is_element_displayed(driver, ORDER_BUTTON)

    def test_login_via_registration_form(self, driver):
        """Вход через кнопку в форме регистрации."""
        # Регистрируем пользователя
        email, password = register_user(driver)
        
        # Логинимся через кнопку в форме регистрации
        driver.get(MAIN_PAGE_URL)
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
        email, password = register_user(driver)
        
        # Логинимся через кнопку в форме восстановления пароля
        driver.get(MAIN_PAGE_URL)
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        wait_for_clickable(driver, RECOVER_PASSWORD_LINK).click()
        wait_for_clickable(driver, LOGIN_LINK_FROM_RECOVER).click()
        
        wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
        wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
        
        # Проверяем, что вошли в аккаунт
        assert is_element_displayed(driver, ORDER_BUTTON)
