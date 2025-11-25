import allure
from DP.alex_talako.pom_site.locators.footer_locators.footer_locators import MainPage

@allure.description("""Этот тест проверяет элементы футера на странице""")
def test_footer(web_browser):


    driver = MainPage(web_browser)
    driver.btn_cookie.click()

    locators = [
        (driver.btn_hands_on_labs, 'Hands-on labs'),
        (driver.btn_for_business, 'For Business'),
        (driver.btn_for_education, 'For Education'),
        (driver.btn_competitive_hacking, 'Competitive Hacking'),
        (driver.btn_defensive_certifications, 'Defensive Certifications'),
        (driver.btn_about_us, 'About Us'),
        (driver.btn_newsroom, 'Newsroom'),
        (driver.btn_blog, 'Blog'),
        (driver.btn_glossary, 'Glossary'),
        (driver.btn_work_at_tryhackme, 'Work at TryHackMe'),
        (driver.btn_careers_in_cyber, 'Careers in Cyber'),
        (driver.btn_buy_vouchers, 'Buy Vouchers'),
        (driver.btn_swag_shop, 'Swag Shop'),
        (driver.btn_contact_us, 'Contact Us'),
        (driver.btn_forum, 'Forum'),
        (driver.btn_privacy_policy, 'Privacy Policy'),
        (driver.btn_terms_of_use, 'Terms of Use'),
        (driver.btn_ai_terms_of_use, 'AI Terms of Use'),
        (driver.btn_acceptable_use_policy, 'Acceptable Use Policy'),
        (driver.btn_cookie_policy, 'Cookie Policy'),
        (driver.btn_follow_us_on_x, ''),
        (driver.btn_linkedin, ''),
        (driver.btn_discord, ''),
        (driver.btn_follow_us_on_facebook, ''),
        (driver.btn_follow_us_on_youtube, ''),
        (driver.btn_follow_us_on_instagram, ''),
        (driver.btn_follow_us_on_pinterest, ''),
        (driver.btn_help_button, ''),
    ]

    for locator, expected_text in locators:
        assert locator.is_visible(), f'Элемент "{expected_text}" отсутствует на экране'
        actual_text = locator.get_text().strip()
        assert actual_text == expected_text, f'Неверный текст. Ожидаемый текст "{expected_text}". Актуальный текст "{actual_text}"'
        assert locator.is_clickable(), f'Элемент "{expected_text}" не кликабелен'