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

        # Открытие формы
        driver.btn_header_consultant.click()

        # Заполнение всех доступных полей формы
        driver.name_input.send_keys('Karl')
        driver.city_input.send_keys('Минск')
        driver.phone_input.send_keys('+375291234567')
        driver.email_input.send_keys('tests@example.com')
        driver.message_textarea.send_keys('Нужна консультация по ремонту')

        # Закрытие формы
        # assert driver.close_button.is_clickable(), 'Кнопка закрытия некликабельна'
        check.is_true(driver.btn_close_consultant.is_visible()), f'{driver.btn_close_consultant} is not visible'
        check.is_true(driver.btn_close_consultant.is_clickable()), f'{driver.btn_close_consultant} is not clickable'
        driver.btn_close_consultant.click()
