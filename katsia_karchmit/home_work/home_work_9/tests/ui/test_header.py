import allure

from katsia_karchmit.home_work.home_work_9.locators.header.header import MainPage
import pytest_check as check

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка элементов на странице хедер')

def test_header(web_browser):


    driver = MainPage(web_browser)

    header_locators = [(driver.btn_header_menu, 'МЕНЮ'),
                       (driver.btn_header_consultant, 'консультант'),

                       ]

    for locator, expected_text in header_locators:
        check.is_true(locator.is_visible()), f'{locator} is not visible'
        check.is_true(locator.is_clickable()), f'{locator} is not clickable'
        actual_text = locator.get_text().strip()
        check.is_true(actual_text == expected_text), f'{actual_text} != {expected_text}'


