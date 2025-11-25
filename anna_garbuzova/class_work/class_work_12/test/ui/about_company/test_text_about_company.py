from anna_garbuzova.class_work.class_work_12.locators.about_company.about_company import AboutPage
import pytest_check as check

def test_text(web_browser):
    # '''Этот тест проверяет текст на странице О компании'''

    driver = AboutPage(web_browser)


    check.equal(driver.text_main_about.get_text(), 'О компании','Неверный текст')