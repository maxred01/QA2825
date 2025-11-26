from katya_maslukovskaya.class_work_12.locators.contacts import contacts
from katya_maslukovskaya.class_work_12.locators.contacts.contacts import Contacts
import pytest_check as check

def test_contacts(web_browser):
    "Этот тест проверяет страницу Контакты"

    driver=Contacts(web_browser)
    locators=[
        (driver.btn_button_minsk),
        (driver.btn_button_gomel),
        (driver.btn_button_grodno),
        (driver.btn_button_brest)

    ]

    for locator in locators:
        check.is_true(locator.is_visible(),'Элемент не виден на странице')
        check.is_true(locator.is_presented(),'Элемент не представлен на странице')
        check.is_true(locator.is_clickable(),'Элемент не кликабелен на странице')


        #проверка на текст

