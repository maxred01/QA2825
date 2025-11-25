from anna_garbuzova.class_work.class_work_12.locators.services.servises import MainPage
import pytest_check as check

def test_header(web_browser):
    # """Этот тест проверяет элементы на странице хедера."""

    driver = MainPage(web_browser)


    check.is_true(driver.btn_header_services.is_visible(), 'Элемент не виден на экране')
    check.is_true(driver.btn_header_services.is_clickable(), 'Элемент не виден на экране')
    check.is_true(driver.btn_header_services.is_presented(), 'Элемент не виден на экране')