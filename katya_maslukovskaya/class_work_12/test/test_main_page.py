import time
import pytest
from termcolor import colored
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from katya_maslukovskaya.class_work_12.page.base_page import WebPage
from katya_maslukovskaya.class_work_12.page.elements import WebElement
from katya_maslukovskaya.class_work_12.page.elements import ManyWebElements
from katya_maslukovskaya.class_work_12.locators.main_page import main_page
from katya_maslukovskaya.class_work_12.locators.main_page.main_page import MainPage
import pytest_check as check

def test_main_page(web_browser):
    """Этот тест проверяет локаторы на главной странице autogroup.by"""

    driver=MainPage(web_browser)
    locators=[
        (driver.btn_header_directions),
        (driver.btn_header_catalog),
        (driver.btn_header_delivery),
        (driver.btn_header_info),
        (driver.btn_header_services),
        (driver.btn_header_payment),
        (driver.btn_header_contacts),
        (driver.btn_header_telegram),
        (driver.btn_header_viber),
        (driver.btn_header_instagram),
        (driver.btn_header_youtube),
        (driver.btn_header_phone_number),
        (driver.btn_body_favorites),
        (driver.btn_body_watch_calatog_auto),
        (driver.btn_body_consultation),
        (driver.btn_body_check_price_auto),
        (driver.btn_body_check_auto),
        (driver.btn_body_link_text),
        (driver.btn_body_auto_for_yourself),
        (driver.btn_body_corporate_auto),
        (driver.btn_body_clear_delivery_pay),
        (driver.btn_body_standart_pay),
        (driver.btn_body_all_included_pay)

    ]

    for locator in locators:
        check.is_true(locator.is_visible(),'элемент не виден на странице')
        check.is_true(locator.is_clickable(),'элемент не кликабелен')
        check.is_true(locator.is_presented(),'элемент не представлен')

