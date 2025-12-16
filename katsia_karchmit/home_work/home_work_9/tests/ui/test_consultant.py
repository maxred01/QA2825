import allure
import time
import random
from selenium.webdriver.common.keys import Keys
from katsia_karchmit.home_work.home_work_9.locators.header.header import MainPage
import pytest_check as check

def generate_unique_data():
    """Генерировать уникальные данные"""
    timestamp = int(time.time())
    return {
        'name': f'Иван{timestamp}',
        'city': f'Минск{random.randint(100, 999)}',
        'phone': f'+37529{random.randint(1000000, 9999999)}',
        'email': f'test{timestamp}@gmail.com',
        'message_textarea': f'Нужна консультация{timestamp}',
    }

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка заполнения формы консультант')

def test_consultant(web_browser):


    driver = MainPage(web_browser)

    #  ОЧИСТКА всех данных браузера
    web_browser.delete_all_cookies()
    web_browser.execute_script("localStorage.clear(); sessionStorage.clear();")
    time.sleep(1)
    web_browser.refresh()
    time.sleep(2)

    # Открытие формы
    driver.btn_header_consultant.click()

    # Генерация НОВЫХ уникальных данных
    test_data = generate_unique_data()

    # Заполнение всех доступных полей формы
    driver.text_name.send_keys(Keys.CONTROL + 'a')
    driver.text_name.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_name.send_keys(test_data['name'])

    driver.text_city.send_keys(Keys.CONTROL + 'a')
    driver.text_city.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_city.send_keys(test_data['city'])

    driver.text_phone.send_keys(Keys.CONTROL + 'a')
    driver.text_phone.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_phone.send_keys(test_data['phone'])

    driver.text_email.send_keys(Keys.CONTROL + 'a')
    driver.text_email.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_email.send_keys(test_data['email'])

    driver.text_message_textarea.send_keys(Keys.CONTROL + 'a')
    driver.text_message_textarea.send_keys(Keys.DELETE)
    time.sleep(0.5)
    driver.text_message_textarea.send_keys(test_data['message_textarea'])
    driver.btn_send.click()

    # Проверка, что появилось сообщение об отправки формы
    check.is_true(driver.text_thank_inquiry.is_visible()), f'{driver.text_thank_inquiry} is not visible'
    time.sleep(3)
    # Возвращаемся на главную страницу
    driver.btn_home_return.click()
    time.sleep(3)
    # Проверяем что вернулись на главную страницу (видна кнопка меню)
    assert driver.btn_header_menu.is_visible(), 'Меню не видно'