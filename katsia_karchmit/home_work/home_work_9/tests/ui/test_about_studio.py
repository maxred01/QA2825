import allure

from katsia_karchmit.home_work.home_work_9.locators.about_studio.about_studio import AboutPage
import pytest_check as check

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка текста на странице о студии')

def test_about_studio(web_browser):
    """Этот тест проверяет правильность текста"""

    driver = AboutPage(web_browser)


    check.equal(driver.text_architectural_bureau.get_text(), 'АРХИТЕКТУРНОЕ БЮРО', 'Неверный текст')
    check.equal(driver.text_zrobim.get_text(), 'ZROBIM', 'Неверный текст')


