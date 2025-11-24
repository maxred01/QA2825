from anna_voytovich.class_work.class_work_12.locators.about_company import AboutPage
from anna_voytovich.class_work.class_work_12.locators.service_services import MainPage
import pytest_check as check


def test_text(web_browser):
    """Этот тест проверяет правильность текста"""

    driver = AboutPage(web_browser)

    check.equal(driver.text_name_about.get_text(), 'О компании', 'Неверный текст')
    check.equal(driver.side_bar_truck.get_text(), 'Грузовые автомобили', 'Неверный текст')
    check.equal(driver.side_bar_spares.get_text(), 'Запасные части', 'Неверный текст')
