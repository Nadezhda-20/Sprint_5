import pytest
from helpers import register_user, login_user, wait_for_clickable, is_element_displayed
from locators import *
from urls import MAIN_PAGE_URL


class TestProfile:
    def test_navigate_to_personal_account(self, driver):
        """Проверь переход по клику на «Личный кабинет»."""
        # Регистрируем и логиним пользователя
        email, password = register_user(driver)
        login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Проверяем, что перешли в личный кабинет
        assert is_element_displayed(driver, PROFILE_LINK)

    def test_navigate_from_profile_to_constructor_via_constructor_button(self, driver):
        """Проверь переход по клику на «Конструктор» из личного кабинета."""
        # Регистрируем и логиним пользователя
        email, password = register_user(driver)
        login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Переходим обратно в конструктор через кнопку "Конструктор"
        wait_for_clickable(driver, CONSTRUCTOR_BUTTON).click()
        
        # Проверяем, что вернулись на главную страницу конструктора
        assert is_element_displayed(driver, HEADER_MAIN)

    def test_navigate_from_profile_to_constructor_via_logo(self, driver):
        """Проверь переход по клику на логотип Stellar Burgers из личного кабинета."""
        # Регистрируем и логиним пользователя
        email, password = register_user(driver)
        login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Переходим обратно в конструктор через логотип
        wait_for_clickable(driver, LOGO_BUTTON).click()
        
        # Проверяем, что вернулись на главную страницу конструктора
        assert is_element_displayed(driver, HEADER_MAIN)

    def test_logout_from_account(self, driver):
        """Проверь выход по кнопке «Выйти» в личном кабинете."""
        # Регистрируем и логиним пользователя
        email, password = register_user(driver)
        login_user(driver, email, password)
        
        # Переходим в личный кабинет
        wait_for_clickable(driver, PERSONAL_ACCOUNT_BUTTON).click()
        
        # Выходим из аккаунта
        wait_for_clickable(driver, LOGOUT_BUTTON).click()
        
        # Проверяем, что вышли из аккаунта (вернулись на страницу логина)
        assert is_element_displayed(driver, HEADER_LOGIN)
