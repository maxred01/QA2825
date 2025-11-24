from anna_voytovich.homework.POM.locators.others.others import MainPage
import pytest_check as check


def test_others(web_browser):

    driver = MainPage(web_browser)

    other_locators = [ (driver.btn_arrow_next, ''),
                        (driver.btn_arrow_previous, ''),
                        (driver.btn_dropdown_tech_characteristics, 'Летно-технические характеристики'),
                        (driver.btn_dropdown_weigh_characteristics, 'Весовые характеристики'),
                        (driver.btn_dropdown_size, 'Габариты'),
                        (driver.btn_leave_an_app,'Оставить заявку'),

    ]

    for locator, expected_text in other_locators:
       check.is_true(locator.is_visible()), f'{locator} is not visible'
       check.is_true(locator.is_clickable()), f'{locator} is not clickable'
       actual_text = locator.get_text().strip()
       check.is_true(actual_text == expected_text), f'{actual_text} != {expected_text}'

