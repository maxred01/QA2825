import time
import allure
import pytest_check as check

from katsia_karchmit.home_work.home_work_9.locators.menu.menu_button import MainPage

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка раздела меню контакты')



def test_contacts_button(web_browser):

    driver = MainPage(web_browser)

    # 1. Открываем меню и переходим в контакты
    driver.menu_button.click()
    time.sleep(2)
    driver.contacts_button.click()
    driver.wait_page_loaded()
    check.is_true(driver.text_contacts_ZROBIM_architects.is_visible()), f'{driver.text_contacts_ZROBIM_architects} is not visible'
    driver._web_driver.execute_script('window.scrollBy(0,3000)')
    time.sleep(3)
    driver.text_field_interest_contacts.send_keys('Возможно трудоустроиться в вашу компанию?')
    driver._web_driver.execute_script('window.scrollBy(0,800)')
    time.sleep(3)
    driver.text_field_name_contacts.send_keys('Иван')
    driver.text_field_city.send_keys('Минск')
    driver.text_field_phone_contacts.send_keys('251235455')
    driver.text_field_email_contacts.send_keys('test_test@gmail.com')
    driver.send_button.click()
    time.sleep(2)
    #Проверка, что появилось сообщение об отправки формы
    check.is_true(driver.text_thank_appeal.is_visible()), f'{driver.text_thank_appeal} is not visible'
    time.sleep(3)
    # 2. Возвращаемся на главную страницу
    driver.home_return_button.click()
    time.sleep(3)
    # 3. Проверяем что вернулись на главную страницу (видна кнопка меню)
    assert driver.menu_button.is_visible(), 'Меню не видно'



