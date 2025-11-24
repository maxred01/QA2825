from anna_voytovich.class_work.class_work_12.locators.service_services import MainPage
import pytest_check as check

def test_header(web_browser):
    '''Этот теcт проверяет элементы на странице хэдера'''

    driver = MainPage(web_browser)

    assert driver.btn_header_service_services.is_visible(), 'Элемент не виден на экране'
