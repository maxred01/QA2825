from DP.anna_voytovich.class_work.POM.locators.footers.footers import MainPage



def test_footer(web_browser):

    driver = MainPage(web_browser)

    footer_locators = [ (driver.btn_footer_advantages, 'ПРЕИМУЩЕСТВА'),
                        (driver.btn_footer_effectivity, 'ЭФЕКТИВНОСТЬ'),
                        (driver.btn_footer_complectation, 'КОМПЛЕКТАЦИИ'),
                        (driver.btn_footer_comfort,'КОМФОРТ'),
                        (driver.btn_footer_the_same_site,'Хочу такой же сайт'),
                        (driver.btn_footer_youtube,''),
                        (driver.btn_footer_vk,''),
    ]

    for locator, expected_text in footer_locators:
       assert locator.is_visible(), f'{locator} is not visible'
       assert locator.is_clickable(), f'{locator} is not clickable'
       actual_text = locator.get_text().strip()
       assert actual_text == expected_text, f'{actual_text} != {expected_text}'

