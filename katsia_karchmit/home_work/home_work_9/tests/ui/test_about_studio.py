import allure
import time
from katsia_karchmit.home_work.home_work_9.locators.about_studio.about_studio import AboutPage
import pytest_check as check

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка текста на странице о студии')

def test_about_studio(web_browser):
    """Этот тест проверяет правильность текста"""

    driver = AboutPage(web_browser)


    check.equal(driver.text_architectural_bureau.get_text(), 'АРХИТЕКТУРНОЕ БЮРО', 'Неверный текст')
    check.equal(driver.text_zrobim.get_text(), 'ZROBIM', 'Неверный текст')

    driver._web_driver.execute_script('window.scrollBy(0,2000)')
    time.sleep(8)
    check.equal(driver.text_architecture_idea.get_text(), 'АРХИТЕКТУРА С ИДЕЕЙ', 'Неверный текст')
    check.equal(driver.text_project_just_beginning.get_text(), 'ПРОЕКТ — ЭТО ТОЛЬКО НАЧАЛО', 'Неверный текст')

    driver._web_driver.execute_script('window.scrollBy(0,3700)')
    time.sleep(8)
    check.equal(driver.text_team.get_text(), 'КОМАНДА', 'Неверный текст')
    check.equal(driver.text_alexey_korablyov.get_text(), 'АЛЕКСЕЙ КОРАБЛЕВ', 'Неверный текст')

    driver._web_driver.execute_script('window.scrollBy(0,5700)')
    time.sleep(8)
    check.equal(driver.text_looking_superprofessional.get_text(), 'Ищем суперпрофессионала, архитектурного фанатика, гения дизайна с КПД 200% в команду архитекторов ZROBIM!', 'Неверный текст')


