import pytest
from helpers import wait_for_element, wait_for_clickable, wait_for_text_to_be_present
from locators import *
from urls import MAIN_PAGE_URL


class TestConstructor:
    def test_switch_to_buns_section(self, driver):
        """Проверь, что работает переход к разделу «Булки»."""
        driver.get(MAIN_PAGE_URL)
        
        # Ждем загрузки главной страницы
        wait_for_element(driver, HEADER_MAIN)
        
        # Переходим в раздел "Соусы" и ждем активации
        wait_for_clickable(driver, SAUCES_SECTION).click()
        wait_for_text_to_be_present(driver, ACTIVE_SECTION, "Соусы")
        
        # Переходим в раздел "Булки" и ждем активации
        wait_for_clickable(driver, BUNS_SECTION).click()
        wait_for_text_to_be_present(driver, ACTIVE_SECTION, "Булки")
        
        # Проверяем, что раздел "Булки" активен
        active_section = wait_for_element(driver, ACTIVE_SECTION)
        assert 'Булки' in active_section.text

    def test_switch_to_sauces_section(self, driver):
        """Проверь, что работает переход к разделу «Соусы»."""
        driver.get(MAIN_PAGE_URL)
        
        # Ждем загрузки главной страницы
        wait_for_element(driver, HEADER_MAIN)
        
        # Переходим в раздел "Соусы" и ждем активации
        wait_for_clickable(driver, SAUCES_SECTION).click()
        wait_for_text_to_be_present(driver, ACTIVE_SECTION, "Соусы")
        
        # Проверяем, что раздел "Соусы" активен
        active_section = wait_for_element(driver, ACTIVE_SECTION)
        assert 'Соусы' in active_section.text

    def test_switch_to_fillings_section(self, driver):
        """Проверь, что работает переход к разделу «Начинки»."""
        driver.get(MAIN_PAGE_URL)
        
        # Ждем загрузки главной страницы
        wait_for_element(driver, HEADER_MAIN)
        
        # Переходим в раздел "Начинки" и ждем активации
        wait_for_clickable(driver, FILLINGS_SECTION).click()
        wait_for_text_to_be_present(driver, ACTIVE_SECTION, "Начинки")
        
        # Проверяем, что раздел "Начинки" активен
        active_section = wait_for_element(driver, ACTIVE_SECTION)
        assert 'Начинки' in active_section.text
