import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time


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


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия драйвера Chrome"""
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


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
