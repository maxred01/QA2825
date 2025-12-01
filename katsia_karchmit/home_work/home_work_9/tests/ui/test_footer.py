import allure
import time

from katsia_karchmit.home_work.home_work_9.locators.footer.footer import MainPage
import pytest_check as check

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка элементов на странице footer')

def test_footer(web_browser):


    driver = MainPage(web_browser)

    footer_locators = [(driver.btn_footer_questionnaire, 'Анкета'),
                       (driver.btn_footer_offer, 'Предложение'),

                       ]

    for locator, expected_text in footer_locators:
        check.is_true(locator.is_visible()), f'{locator} is not visible'
        check.is_true(locator.is_clickable()), f'{locator} is not clickable'
        actual_text = locator.get_text().strip()
        check.is_true(actual_text == expected_text), f'{actual_text} != {expected_text}'

        # Открытие формы
        driver.btn_footer_questionnaire.click()
        # 2. Заполняем анкету соискателя
        driver.text_field_name.send_keys('Karl')
        check.is_true(driver.text_field_name.is_visible()), f'{driver.text_field_name} is not visible'
        driver.text_field_surname.send_keys('Franz')
        check.is_true(driver.text_field_surname.is_visible()), f'{driver.text_field_surname} is not visible'
        driver.next_button.click()
        time.sleep(5)
        driver.text_field_job.send_keys('Engineer')
        check.is_true(driver.text_field_job.is_visible()), f'{driver.text_field_job} is not visible'
        driver.text_field_link_portfolio.send_keys('https://bntu.by/index.php/news/3036-ya-inzhener')
        driver.further_button.click()
        time.sleep(5)
        driver.text_field_phone.send_keys('+375291585525')
        check.is_true(driver.text_field_phone.is_visible()), f'{driver.text_field_phone} is not visible'
        driver.text_field_email.send_keys('test_test@gmail.com')
        check.is_true(driver.text_field_email.is_visible()), f'{driver.text_field_email} is not visible'