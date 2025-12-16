import allure
import time
import random
from selenium.webdriver.common.keys import Keys
from katsia_karchmit.home_work.home_work_9.locators.footer.footer import MainPage
import pytest_check as check

def generate_unique_data():
    """Генерировать уникальные данные"""
    timestamp = int(time.time())
    return {
        'name': f'Иван{timestamp}',
        'surname': f'Иванов{random.randint(100, 999)}',
        'job': f'Архитектор{timestamp}',
        'portfolio': f'https://test{timestamp}.com',
        'phone': f'+37529{random.randint(1000000, 9999999)}',
        'email': f'test{timestamp}@gmail.com'
    }


@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка заполнения формы Анкета')


def test_questionnaire(web_browser):
    driver = MainPage(web_browser)

    # 1. ОЧИСТКА всех данных браузера
    web_browser.delete_all_cookies()
    web_browser.execute_script("localStorage.clear(); sessionStorage.clear();")
    time.sleep(1)
    web_browser.refresh()
    time.sleep(2)

    # 2. Скролл к футеру
    driver._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.btn_footer_questionnaire.click()
    time.sleep(5)

    # 5. Генерация НОВЫХ уникальных данных
    test_data = generate_unique_data()

    # 6. Заполнение формы с ОЧИСТКОЙ полей
    # Поле Имя
    driver.text_field_name.send_keys(Keys.CONTROL + 'a')
    driver.text_field_name.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_field_name.send_keys(test_data['name'])
    check.is_true(driver.text_field_name.is_visible(), 'Поле имени не видно')
    time.sleep(1)

    # Поле Фамилия
    driver.text_field_surname.send_keys(Keys.CONTROL + 'a')
    driver.text_field_surname.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_field_surname.send_keys(test_data['surname'])
    check.is_true(driver.text_field_surname.is_visible(), 'Поле фамилии не видно')
    time.sleep(1)

    # Кнопка Далее
    driver.next_button.click()
    time.sleep(3)

    # Поле Должность
    driver.text_field_job.send_keys(Keys.CONTROL + 'a')
    driver.text_field_job.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_field_job.send_keys(test_data['job'])
    check.is_true(driver.text_field_job.is_visible(), 'Поле должности не видно')
    time.sleep(1)

    # Поле Портфолио
    driver.text_field_link_portfolio.send_keys(Keys.CONTROL + 'a')
    driver.text_field_link_portfolio.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_field_link_portfolio.send_keys(test_data['portfolio'])
    check.is_true(driver.text_field_link_portfolio.is_visible(), 'Поле портфолио не видно')
    time.sleep(1)

    # Кнопка Продолжить
    driver.further_button.click()
    time.sleep(3)

    # Поле Телефон
    driver.text_field_phone.send_keys(Keys.CONTROL + 'a')
    driver.text_field_phone.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_field_phone.send_keys(test_data['phone'])
    check.is_true(driver.text_field_phone.is_visible(), 'Поле телефона не видно')
    time.sleep(1)

    # Поле Email
    driver.text_field_email.send_keys(Keys.CONTROL + 'a')
    driver.text_field_email.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_field_email.send_keys(test_data['email'])
    check.is_true(driver.text_field_email.is_visible(), 'Поле email не видно')
    time.sleep(1)

    # Отправка формы
    driver.btn_send.click()
    time.sleep(5)

    # Проверка результата
    driver.text_thank_you.is_presented()
    check.is_true(driver.text_thank_you.is_visible(), 'Сообщение "Спасибо" не видно на странице')
