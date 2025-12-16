import allure
import time
from katsia_karchmit.home_work.home_work_9.locators.footer.footer import MainPage
import pytest_check as check


@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка элементов на странице footer')

def test_footer(web_browser):
    driver = MainPage(web_browser)

    # Скролл к футеру
    driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

    #  Проверка элементов футера
    footer_locators = [
        (driver.btn_footer_questionnaire, 'Анкета'),
        (driver.btn_footer_offer, 'Предложение'),
        (driver.text_order_project, 'ЗАКАЗАТЬ ПРОЕКТ'),
        (driver.text_cooperation, 'СОТРУДНИЧЕСТВО'),
        (driver.btn_footer_language, 'ЯЗЫК'),
    ]

    for locator, expected_text in footer_locators:
        if not locator.is_presented():
            print(f"Элемент '{expected_text}' не найден")
            continue

        check.is_true(locator.is_visible(), f'{expected_text} не виден')
        check.is_true(locator.is_clickable(), f'{expected_text} не кликабелен')
        actual_text = locator.get_text().strip()
        check.is_true(actual_text == expected_text, f'Текст не совпадает: "{actual_text}" != "{expected_text}"')


