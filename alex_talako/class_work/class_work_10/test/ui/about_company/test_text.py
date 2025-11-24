from alex_talako.class_work.class_work_10.locators.about_company.about_company import AboutPage
import pytest_check as check


def test_text(web_browser):
    """Этот тест проверяет правильность текста"""

    driver = AboutPage(web_browser)

    check.equal(driver.text_name_about.get_text(), 'О компании', 'Неверный текст')
    check.equal(driver.text_side_bar_1.get_text(), 'Грузовые автомобили', 'Неверный текст')
    check.equal(driver.text_side_bar_2.get_text(), 'Запассные части', 'Неверный текст')
    check.equal(driver.text_side_bar_3.get_text(), 'Масла и т.д.', 'Неверный текст')
    check.equal(driver.text_side_bar_4.get_text(), 'Сервис Scania', 'Неверный текст')
