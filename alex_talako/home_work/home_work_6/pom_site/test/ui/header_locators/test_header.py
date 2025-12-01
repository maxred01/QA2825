import allure
from DP.alex_talako.pom_site.locators.header_locators.header_locators import MainPage


@allure.description("""Этот тест проверяет элементы хэдера на странице""")
def test_header(web_browser):


    driver = MainPage(web_browser)
    driver.btn_cookie.click()

    locators = [
        (driver.btn_header_hacktivities, 'Learn'),
        (driver.btn_header_practice, 'Practice'),
        (driver.btn_header_compete, 'Compete'),
        (driver.btn_header_education, 'Education'),
        (driver.btn_header_business, 'Business'),
        (driver.btn_header_pricing, 'Pricing'),
        (driver.btn_header_search, ''),
        (driver.btn_header_log_in, 'Log In'),
        (driver.btn_header_join_for_free, 'Join for FREE'),
    ]

    for locator, expected_text in locators:
        assert locator.is_visible(), f'Элемент "{expected_text}" отсутствует на экране'
        actual_text = locator.get_text().strip()
        assert actual_text == expected_text, f'Неверный текст. Ожидаемый текст "{expected_text}". Актуальный текст "{actual_text}"'
        assert locator.is_clickable(), f'Элемент "{expected_text}" не кликабелен'


