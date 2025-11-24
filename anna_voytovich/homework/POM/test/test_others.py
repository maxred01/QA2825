from DP.anna_voytovich.class_work.POM.locators.others.others import MainPage



def test_others(web_browser):

    driver = MainPage(web_browser)

    other_locators = [ (driver.btn_arrow_next, ''),
                        (driver.btn_arrow_previous, ''),
                        (driver.btn_dropdown_tech_characteristics, 'Летно-технические характеристики'),
                        (driver.btn_dropdown_weigh_characteristics, 'Весовые характеристики'),
                        (driver.btn_dropdown_size, ''),
                        (driver.btn_leave_an_app,'Оставить заявку'),

    ]

    for locator, expected_text in other_locators:
       assert locator.is_visible(), f'{locator} is not visible'
       assert locator.is_clickable(), f'{locator} is not clickable'
       actual_text = locator.get_text().strip()
       assert actual_text == expected_text, f'{actual_text} != {expected_text}'

