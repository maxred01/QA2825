from anna_voytovich.homework.POM.locators.headers.headers import MainPage



def test_header(web_browser):

    driver = MainPage(web_browser)

    header_locators = [ (driver.btn_header_advantages, 'ПРЕИМУЩЕСТВА'),
                        (driver.btn_header_effectivity, 'ЭФФЕКТИВНОСТЬ'),
                        (driver.btn_header_complectation, 'КОМПЛЕКТАЦИЯ'),
                        (driver.btn_header_comfort,'КОМФОРТ'),
                        (driver.btn_header_buy,'КУПИТЬ В ЛИЗИНГ'),
    ]

    for locator, expected_text in header_locators:
       assert locator.is_visible(), f'{locator} is not visible'
       assert locator.is_clickable(), f'{locator} is not clickable'
       actual_text = locator.get_text().strip()
       assert actual_text == expected_text, f'{actual_text} != {expected_text}'