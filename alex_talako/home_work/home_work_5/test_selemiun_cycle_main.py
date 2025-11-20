import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_CONST = 'https://tryhackme.com/'

def test_selenium_with_cycle():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://tryhackme.com/')
    time.sleep(3)
    driver.find_element((By.XPATH, '//button[contains(., "Got it!")]')).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Learn page"]').click()
    time.sleep(2)
    data_learn = [
        (driver.find_element(By.XPATH, '(//*[@aria-selected="false"])[1]'), 'Paths', 'hacktivities?tab=paths'),
        (driver.find_element(By.XPATH, '(//*[@aria-selected="false"])[2]'), 'Modules','hacktivities?tab=modules'),
        (driver.find_element(By.XPATH, '//*[@aria-orientation="horizontal"]/*[4]'),'Walkthroughs','hacktivities?tab=rooms'),
        (driver.find_element(By.XPATH, '//*[@aria-orientation="horizontal"]/*[5]'),'Networks', 'hacktivities?tab=network'),
    ]

    for element, text, url in data_learn:
        element.click()
        time.sleep(3)
        assert element.is_displayed(), f'Элемент {text} отсутствует'
        assert element.is_enabled(), f'Элемент {text} не кликабелен'
        assert driver.current_url == URL_CONST + url, f'Неверная ссылка {text}'

    practice_button = driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Practice"]')
    assert practice_button.is_displayed(), 'Элемент отсутствует'
    assert practice_button.is_enabled(), 'Элемент не кликабелен'
    assert practice_button.text == 'Practice', f"Неверный текст. Получено {practice_button}"
    practice_button.click()
    time.sleep(2)

    challenges_button = driver.find_element(By.XPATH, '(//*[@data-testid="splitScreenMiddle"]//*[@type="main"])[1]')
    assert challenges_button.is_displayed(), 'Элемент отсутствует'
    assert challenges_button.is_enabled(), 'Элемент не кликабелен'
    assert challenges_button.text == 'Challenges\nReinforce your learning', f"Неверный текст. Получено {challenges_button}"
    challenges_button.click()
    time.sleep(4)
    practice_button.click()
    time.sleep(2)

    soc_simulator_button = driver.find_element(By.XPATH,'(//*[@type="main"])[3]')
    assert soc_simulator_button.is_displayed(), 'Элемент отсутствует'
    assert soc_simulator_button.is_enabled(), 'Элемент не кликабелен'
    assert soc_simulator_button.text == 'SOC Simulator\nTriage alerts in realtime', f"Неверный текст. Получено {soc_simulator_button}"
    soc_simulator_button.click()
    time.sleep(4)
    practice_button.click()
    time.sleep(2)

    threat_button = driver.find_element(By.XPATH,'(//*[@type="main"])[5]')
    assert threat_button.is_displayed(),'Элемент отсутствует'
    assert threat_button.is_enabled(),'Элемент не кликабелен'
    assert threat_button.text == 'Threat Hunting Simulator\nNEW\nReconstruct the attack chain', f"Неверный текст. Получено {threat_button}"
    threat_button.click()
    time.sleep(2)

    data_threat = [
        ('Scenarios', 'threat-hunting-sim/scenarios'),
        ('Progress and stats', 'threat-hunting-sim/stats'),
        ('Leaderboard', 'threat-hunting-sim/leaderboard'),
    ]
    for text, url in data_threat:
        link_xpath = f'//a[contains(text(), "{text}")]'
        element = driver.find_element(By.XPATH, link_xpath)
        assert element.is_displayed(), f'Элемент {text} отсутствует'
        assert element.is_enabled(), f'Элемент {text} не кликабелен'
        element.click()
        time.sleep(2)
        assert driver.current_url == URL_CONST + url, f'Неверная ссылка {text}'
        driver.back()
        time.sleep(2)
    practice_button.click()
    time.sleep(2)

    certified_button = driver.find_element(By.XPATH,'//*[@aria-orientation="vertical"]//*[@aria-haspopup="menu"]/*[1]')
    assert certified_button.is_displayed(),'Элемент отсутствует'
    assert certified_button.is_enabled(), 'Элемент не кликабелен'
    assert certified_button.text == 'Get certified\nVerify your skills', f"Неверный текст. Получено {certified_button}"
    certified_button.click()
    time.sleep(2)

    pt_button = driver.find_element(By.XPATH,'(//*[@type="other"])[1]')
    assert pt_button.is_displayed(),'Элемент отсутствует'
    assert pt_button.is_enabled(),'Элемент не кликабелен'
    assert pt_button.text == 'PT1\nJr Penetration Tester Certificate', f"Неверный текст. Получено {pt_button}"
    pt_button.click()
    time.sleep(4)
    practice_button.click()
    time.sleep(2)

    sal_button = driver.find_element(By.XPATH,'(//*[@type="other"])[3]')
    assert sal_button.is_displayed(),'Элемент отсутствует'
    assert sal_button.is_enabled(), 'Элемент не кликабелен'
    assert sal_button.text == 'SAL1\nSecurity Analyst Level 1 Certificate', f"Неверный текст. Получено {sal_button}"
    sal_button.click()
    time.sleep(4)
    practice_button.click()
    time.sleep(2)

    tabletop_button = driver.find_element(By.XPATH,'(//*[@type="main"])[9]')
    assert tabletop_button.is_displayed(),'Элемент отсутствует'
    assert tabletop_button.is_enabled(),'Элемент не кликабелен'
    assert tabletop_button.text == 'Tabletop Exercises\nNEW\nTest response readiness',f"Неверный текст. Получено {tabletop_button}"
    tabletop_button.click()
    time.sleep(2)

    data_table = [
        ('Exercises', 'tabletop-exercises/exercises'),
        ('Profiles', 'tabletop-exercises/profiles'),
        ('Reports', 'tabletop-exercises/reports'),
    ]
    for text, url in data_table:
        link_xpath = f'//a[contains(text(), "{text}")]'
        element = driver.find_element(By.XPATH, link_xpath)
        assert element.is_displayed(), f'Элемент {text} отсутствует'
        assert element.is_enabled(), f'Элемент {text} не кликабелен'
        element.click()
        time.sleep(2)
        assert driver.current_url == URL_CONST + url, f'Неверная ссылка {text}'
        driver.back()
        time.sleep(2)


    compete_button = driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Compete"]')
    assert compete_button.is_displayed(), 'Элемент отсутствует'
    assert compete_button.is_enabled(), 'Элемент не кликабелен'
    assert compete_button.text == 'Compete', f"Неверный текст. Получено {compete_button}"
    compete_button.click()
    time.sleep(2)

    compete_king_button = driver.find_element(By.XPATH, '(//*[@type="main"])[1]')
    assert compete_king_button.is_displayed(), 'Элемент отсутствует'
    assert compete_king_button.is_enabled(), 'Элемент не кликабелен'
    assert compete_king_button.text, 'King of the Hill\nAttack & Defend'
    compete_king_button.click()
    time.sleep(4)
    compete_button.click()
    time.sleep(2)

    leaderboards_button = driver.find_element(By.XPATH, '(//*[@type="main"])[3]')
    assert leaderboards_button.is_displayed(),'Элемент отсутствует'
    assert leaderboards_button.is_enabled(),'Элемент не кликабелен'
    assert leaderboards_button.text == 'Leaderboards\nPlatform Rankings', f"Неверный текст. Получено {leaderboards_button}"
    leaderboards_button.click()
    time.sleep(2)

    education_button = driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Education"]')
    assert education_button.is_displayed(), 'Элемент отсутствует'
    assert education_button.is_enabled(), 'Элемент не кликабелен'
    assert education_button.text == 'Education', f"Неверный текст. Получено {education_button}"
    education_button.click()
    time.sleep(2)

    teaching_button = driver.find_element(By.XPATH, '(//*[@data-testid="splitScreenMiddle"]//*[@type="main"])[1]')
    assert teaching_button.is_displayed(), 'Элемент отсутствует'
    assert teaching_button.is_enabled(), 'Элемент не кликабелен'
    assert teaching_button.text == 'Teaching\nUse our security labs', f"Неверный текст. Получено {teaching_button}"
    teaching_button.click()
    time.sleep(2)

    business_button = driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Business page"]')
    assert business_button.is_displayed(), 'Элемент отсутствует'
    assert business_button.is_enabled(), 'Элемент не кликабелен'
    assert business_button.text == 'Business', f"Неверный текст. Получено {business_button}"
    business_button.click()
    time.sleep(3)

    pricing_button = driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Pricing page"]')
    assert pricing_button.is_displayed(), 'Элемент отсутствует'
    assert pricing_button.is_enabled(), 'Элемент не кликабелен'
    assert pricing_button.text == 'Pricing', f"Неверный текст. Получено {pricing_button}"
    pricing_button.click()
    time.sleep(3)

    search_button = driver.find_element(By.XPATH, '//*[@data-testid="search-btn"]')
    assert search_button.is_displayed(), 'Элемент отсутствует'
    assert search_button.is_enabled(), 'Элемент не кликабелен'
    assert search_button.text == '', f"Неверный текст. Получено {search_button}"
    search_button.click()
    driver.find_element(By.XPATH, '//*[@data-testid="search-input"]').send_keys('rock')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@data-testid="search-input"]').clear()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@data-testid="search-input"]').send_keys('kali')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@data-testid="search-input"]').send_keys(Keys.ENTER)
    time.sleep(3)
    driver.execute_script("""
                       Array.from(document.querySelectorAll('*')).find(el => 
                           ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                       )?.scrollBy(0,500);
                   """)
    time.sleep(3)
    driver.find_element(By.XPATH, '(//*[@data-testid="new-content"]//a)[1]').click()
    time.sleep(3)

    authorization_button = driver.find_element(By.XPATH, '(//*[@data-link="outlined"])[2]')
    assert authorization_button.is_displayed(), 'Элемент отсутствует'
    assert authorization_button.is_enabled(), 'Элемент не кликабелен'
    assert authorization_button.text == 'Log In', f"Неверный текст. Получено {authorization_button}"
    authorization_button.click()
    time.sleep(3)

    join_button = driver.find_element(By.XPATH, '//*[@data-link="join"]')
    assert join_button.is_displayed(), 'Элемент отсутствует'
    assert join_button.is_enabled(), 'Элемент не кликабелен'
    assert join_button.text == 'Join for FREE', f"Неверный текст. Получено {join_button}"
    join_button.click()
    time.sleep(3)


    driver.close()
    driver.quit()
