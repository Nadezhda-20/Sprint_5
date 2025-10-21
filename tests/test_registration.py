import pytest
from helpers import generate_email, generate_password, generate_name, wait_for_element, wait_for_clickable, is_element_displayed
from locators import *
from urls import LOGIN_PAGE_URL


class TestRegistration:
    def test_successful_registration(self, driver):
        """Успешная регистрация. Поле «Имя» не пустое; email в формате логин@домен; пароль — шесть символов."""
        # Генерируем валидные данные
        email = generate_email()
        password = generate_password(6)
        name = generate_name()
        
        # Переходим к регистрации
        driver.get(MAIN_PAGE_URL)
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        wait_for_clickable(driver, REGISTER_LINK).click()
        
        # Заполняем форму регистрации
        wait_for_element(driver, NAME_INPUT_REGISTER).send_keys(name)
        wait_for_element(driver, EMAIL_INPUT_REGISTER).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_REGISTER).send_keys(password)
        wait_for_clickable(driver, REGISTER_BUTTON).click()
        
        # Проверяем, что перешли на страницу логина после успешной регистрации
        assert is_element_displayed(driver, HEADER_LOGIN)
        assert driver.current_url == LOGIN_PAGE_URL

    @pytest.mark.xfail(reason="Баг сайта: регистрация с паролем менее 6 символов проходит успешно")
    def test_registration_with_short_password(self, driver):
        """Ошибка для некорректного пароля (меньше 6 символов)."""
        # Генерируем данные с коротким паролем
        email = generate_email()
        password = generate_password(5)  # Пароль меньше 6 символов
        name = generate_name()
        
        # Переходим к регистрации
        driver.get(MAIN_PAGE_URL)
        wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
        wait_for_clickable(driver, REGISTER_LINK).click()
        
        # Заполняем форму регистрации
        wait_for_element(driver, NAME_INPUT_REGISTER).send_keys(name)
        wait_for_element(driver, EMAIL_INPUT_REGISTER).send_keys(email)
        wait_for_element(driver, PASSWORD_INPUT_REGISTER).send_keys(password)
        wait_for_clickable(driver, REGISTER_BUTTON).click()
        
        # Ждем стабилизации - используем ожидание вместо time.sleep
        wait_for_element(driver, REGISTER_BUTTON)
        
        # Проверяем, что остались на странице регистрации (не перешли на логин)
        current_url = driver.current_url
        assert 'register' in current_url, f"Ожидалось остаться на странице регистрации, но текущий URL: {current_url}"
