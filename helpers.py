import random
import string
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import *
from urls import *


def generate_email():
    """Генерирует уникальный email для регистрации"""
    timestamp = int(time.time())
    random_string = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"nadezhda_lapukina_{timestamp}_{random_string}@yandex.ru"


def generate_password(length=6):
    """Генерирует пароль указанной длины"""
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def generate_name():
    """Генерирует случайное имя"""
    names = ['Анна', 'Иван', 'Мария', 'Петр', 'Ольга', 'Сергей', 'Елена', 'Дмитрий']
    return random.choice(names)


def wait_for_element(driver, locator, timeout=10):
    """Ожидает появления элемента на странице"""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_for_clickable(driver, locator, timeout=10):
    """Ожидает, когда элемент станет кликабельным"""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def is_element_displayed(driver, locator, timeout=5):
    """Проверяет, отображается ли элемент на странице"""
    try:
        wait_for_element(driver, locator, timeout)
        return True
    except:
        return False


def wait_for_text_to_be_present(driver, locator, text, timeout=10):
    """Ожидает, пока элемент не будет содержать определенный текст"""
    return WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator, text))


def wait_for_element_to_be_selected(driver, locator, timeout=10):
    """Ожидает, пока элемент не будет выбран/активен"""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_selected(locator))


def register_user(driver):
    """Регистрирует нового пользователя и возвращает данные"""
    email = generate_email()
    password = generate_password(8)
    name = generate_name()
    
    # Регистрируем пользователя
    driver.get(MAIN_PAGE_URL)
    wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
    wait_for_clickable(driver, REGISTER_LINK).click()
    
    wait_for_element(driver, NAME_INPUT_REGISTER).send_keys(name)
    wait_for_element(driver, EMAIL_INPUT_REGISTER).send_keys(email)
    wait_for_element(driver, PASSWORD_INPUT_REGISTER).send_keys(password)
    wait_for_clickable(driver, REGISTER_BUTTON).click()
    
    # Ждем перехода на страницу логина
    wait_for_element(driver, HEADER_LOGIN)
    
    return email, password


def login_user(driver, email, password):
    """Логинит пользователя"""
    driver.get(MAIN_PAGE_URL)
    wait_for_clickable(driver, LOGIN_BUTTON_MAIN).click()
    
    wait_for_element(driver, EMAIL_INPUT_LOGIN).send_keys(email)
    wait_for_element(driver, PASSWORD_INPUT_LOGIN).send_keys(password)
    wait_for_clickable(driver, LOGIN_BUTTON_FORM).click()
    
    # Ждем загрузки главной страницы после логина
    wait_for_element(driver, HEADER_MAIN)
