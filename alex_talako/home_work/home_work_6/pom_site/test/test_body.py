import time
from alex_talako.home_work.home_work_6.pom_site.locators.body_locators.body_locators import MainPage


def test_other_locators(web_browser):
    """Этот тест проверяет остальные локаторы на странице, кроме хэдера и футера"""

    driver = MainPage(web_browser)
    driver.btn_cookie.click()

    locators = [
        (driver.btn_email,''),
        (driver.btn_join_near_email,'Join for FREE'),
        (driver.btn_container_cyber_security,'Cyber Security 101\nEnroll in Path'),
        (driver.btn_soc_level_one,'SOC Level 1\nEnroll in Path'),
        (driver.btn_pre_security,'Pre Security\nEnroll in Path'),
        (driver.btn_dot_first, ''),
        (driver.btn_dot_second, ''),
        (driver.btn_dot_third, ''),
        (driver.btn_dot_fourth, ''),
        (driver.btn_dot_fifth, ''),
        (driver.btn_exercises_in_lesson, 'Exercises in every lesson'),
        (driver.btn_beginner_friendly, 'Beginner-friendly'),
        (driver.btn_start_hacking_instantly, 'Start hacking instantly'),
        (driver.btn_real_world_networks, 'Real-world networks'),
        (driver.btn_dot_bottom_first, ''),
        (driver.btn_dot_bottom_second, ''),
        (driver.btn_dot_bottom_third, ''),
        (driver.btn_cyber_train_for_team, 'Learn More'),
        (driver.btn_cyber_tarin_for_students, 'Learn More'),
        (driver.btn_bottom_join_for_free, 'Join for FREE'),
        ]

    for locator, expected_text in locators:
        assert locator.is_visible(), f'Элемент "{expected_text}" отсутствует на экране'
        actual_text = locator.get_text().strip()
        assert actual_text == expected_text, f'Неверный текст. Ожидаемый текст "{expected_text}". Актуальный текст "{actual_text}"'
        assert locator.is_clickable(), f'Элемент "{expected_text}" не кликабелен'

    driver.btn_dot_second.click()
    time.sleep(1)

    locators_after_click_dot_1 = [
        (driver.btn_jr_penetration_tester,'Jr Penetration Tester\nEnroll in Path'),
        (driver.btn_red_teaming,'Red Teaming\nEnroll in Path'),
        (driver.btn_soc_level_two,'SOC Level 2\nEnroll in Path'),
        ]

    for locator, expected_text in locators_after_click_dot_1:
        assert locator.is_visible(), f'Элемент "{expected_text}" отсутствует на экране'
        actual_text = locator.get_text().strip()
        assert actual_text == expected_text, f'Неверный текст. Ожидаемый текст "{expected_text}". Актуальный текст "{actual_text}"'
        assert locator.is_clickable(), f'Элемент "{expected_text}" не кликабелен'

    driver.btn_dot_third.click()
    time.sleep(1)

    locators_after_click_dot_2 = [
        (driver.btn_security_engineer,'Security Engineer\nEnroll in Path'),
        (driver.btn_dev_sec_ops,'DevSecOps\nEnroll in Path'),
        (driver.btn_advanced_endpoint,'Advanced Endpoint Investigations\nEnroll in Path'),
        ]

    for locator, expected_text in locators_after_click_dot_2:
        assert locator.is_visible(), f'Элемент "{expected_text}" отсутствует на экране'
        actual_text = locator.get_text().strip()
        assert actual_text == expected_text, f'Неверный текст. Ожидаемый текст "{expected_text}". Актуальный текст "{actual_text}"'
        assert locator.is_clickable(), f'Элемент "{expected_text}" не кликабелен'

    driver.btn_dot_fourth.click()
    time.sleep(1)

    locators_after_click_dot_3 = [
        (driver.btn_defending_azure,'Defending Azure\nEnroll in Path'),
        (driver.btn_att_def_aws,'Attacking and Defending AWS\nEnroll in Path'),
        (driver.btn_offensive_pentest,'Offensive Pentesting\nEnroll in Path'),
        ]

    for locator, expected_text in locators_after_click_dot_3:
        assert locator.is_visible(), f'Элемент "{expected_text}" отсутствует на экране'
        actual_text = locator.get_text().strip()
        assert actual_text == expected_text, f'Неверный текст. Ожидаемый текст "{expected_text}". Актуальный текст "{actual_text}"'
        assert locator.is_clickable(), f'Элемент "{expected_text}" не кликабелен'

    driver.btn_dot_fifth.click()
    time.sleep(1)

    locators_after_click_dot_4 = [
        (driver.btn_web_fundamentals, 'Web Fundamentals\nEnroll in Path'),
        (driver.btn_web_application, 'Web Application Pentesting\nEnroll in Path'),
        (driver.btn_comp_tia, 'CompTIA Pentest+\nEnroll in Path'),
        ]

    for locator, expected_text in locators_after_click_dot_4:
        assert locator.is_visible(), f'Элемент "{expected_text}" отсутствует на экране'
        actual_text = locator.get_text().strip()
        assert actual_text == expected_text, f'Неверный текст. Ожидаемый текст "{expected_text}". Актуальный текст "{actual_text}"'
        assert locator.is_clickable(), f'Элемент "{expected_text}" не кликабелен'