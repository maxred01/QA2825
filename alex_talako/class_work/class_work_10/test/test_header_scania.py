from alex_talako.class_work.class_work_10.locators.services.services import MainPage
import pytest_check as check


def test_header(web_browser):
    """Этот тест проверяет элементы на странице хэдера"""

    driver = MainPage(web_browser)

    # assert driver.btn_header_services.is_visible(), 'Элемент отсутствует на экране'
    check.is_false(driver.btn_header_services.is_visible, 'Элемент отсутствует на экране')
    check.is_false(driver.btn_header_services.is_clickable(), 'Элемент отсутствует на экране')
    check.is_false(driver.btn_header_services.is_presented(), 'Элемент отсутствует на экране')