import pytest
from conftest import wait_for_element, wait_for_clickable
from locators import *
import time


class TestConstructor:
    def test_switch_to_buns_section(self, driver):
        """Проверь, что работает переход к разделу «Булки»."""
        driver.get("https://stellarburgers.education-services.ru")
        
        # Добавляем небольшую паузу для полной загрузки
        time.sleep(2)
        
        # Переходим в раздел "Соусы"
        wait_for_clickable(driver, SAUCES_SECTION).click()
        
        # Ждем немного для переключения
        time.sleep(1)
        
        # Переходим в раздел "Булки"
        wait_for_clickable(driver, BUNS_SECTION).click()
        
        # Ждем немного для переключения
        time.sleep(1)
        
        # Проверяем, что раздел "Булки" активен
        active_section = wait_for_element(driver, ACTIVE_SECTION)
        active_text = active_section.text
        
        # Дополнительная проверка: если все еще "Соусы", попробуем еще раз
        if 'Соусы' in active_text:
            time.sleep(1)
            wait_for_clickable(driver, BUNS_SECTION).click()
            time.sleep(1)
            active_section = wait_for_element(driver, ACTIVE_SECTION)
            active_text = active_section.text
        
        assert 'Булки' in active_text, f"Ожидался активный раздел 'Булки', но получен: {active_text}"

    def test_switch_to_sauces_section(self, driver):
        """Проверь, что работает переход к разделу «Соусы»."""
        driver.get("https://stellarburgers.education-services.ru")
        
        # Добавляем небольшую паузу для полной загрузки
        time.sleep(2)
        
        # Переходим в раздел "Соусы"
        wait_for_clickable(driver, SAUCES_SECTION).click()
        
        # Ждем немного для переключения
        time.sleep(1)
        
        # Проверяем, что раздел "Соусы" активен
        active_section = wait_for_element(driver, ACTIVE_SECTION)
        assert 'Соусы' in active_section.text

    def test_switch_to_fillings_section(self, driver):
        """Проверь, что работает переход к разделу «Начинки»."""
        driver.get("https://stellarburgers.education-services.ru")
        
        # Добавляем небольшую паузу для полной загрузки
        time.sleep(2)
        
        # Переходим в раздел "Начинки"
        wait_for_clickable(driver, FILLINGS_SECTION).click()
        
        # Ждем немного для переключения
        time.sleep(1)
        
        # Проверяем, что раздел "Начинки" активен
        active_section = wait_for_element(driver, ACTIVE_SECTION)
        assert 'Начинки' in active_section.text
