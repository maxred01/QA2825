import time
from katsia_karchmit.home_work.home_work_9.locators.menu.menu_button import MainPage




def test_contacts_button(web_browser):
    '''Этот тест проверяет раздел меню контакты'''
    driver = MainPage(web_browser)

    # 1. Открываем меню и переходим в проекты
    driver.menu_button.click()
    time.sleep(2)
    driver.contacts_button.click()
    driver.wait_page_loaded()
    driver._web_driver.execute_script('window.scrollBy(0,3000)')
    time.sleep(3)
    driver.text_field_interest_contacts.send_keys('Work in your company?')
    driver._web_driver.execute_script('window.scrollBy(0,800)')
    time.sleep(3)
    driver.text_field_name_contacts.send_keys('Karl')
    driver.text_field_city.send_keys('Minsk')
    driver.text_field_phone_contacts.send_keys('251235455')
    driver.text_field_email_contacts.send_keys('test_test@gmail.com')
    # 2. Возвращаемся в меню
    driver._web_driver.execute_script('window.scrollBy(0,1500)')
    time.sleep(3)
    driver.menu_button.click()
    time.sleep(8)

    # 3. Проверяем что меню открылось (виден какой-то пункт меню)
    assert driver.contacts_button.is_visible(), 'Меню не открылось после возврата'



