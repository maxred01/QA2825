from katsia_karchmit.class_work.class_work_12.locators.service_services.service_services import MainPage
import pytest_check as check
def test_header(web_browser):
    '''Этот тест проверяет элемент на странице хедер'''

    driver = MainPage(web_browser)

    check.is_false(driver.btn_header_service_services.is_visible(), 'Элемент не виден на экране')
    check.is_true(driver.btn_header_service_services.is_clickable(), 'Элемент не виден на экране')
    check.is_true(driver.btn_header_service_services.is_presented(), 'Элемент не виден на экране')
