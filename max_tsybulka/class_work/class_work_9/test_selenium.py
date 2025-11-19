import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_selenium():

    driver = webdriver.Chrome()
    driver.get('https://pm.by/ru/')
    time.sleep(10)
    data = [
        (driver.find_element(By.ID, 'cookiescript_accept'), 'кнопка привет'),
        (driver.find_element(By.ID, 'cookiescript_accept'), 'кнопка привет'),
        (driver.find_element(By.ID, 'cookiescript_accept'), 'кнопка привет'),
        (driver.find_element(By.ID, 'cookiescript_accept'), 'кнопка привет'),
        (driver.find_element(By.ID, 'cookiescript_accept'), 'кнопка привет'),
            ]

    driver.find_element(By.ID, 'cookiescript_accept').click()
    driver.find_element(By.XPATH, '//i[@class="digi_icon-close"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@class="missions-tooltip__button"]').click()
    driver.find_element(By.XPATH, '//div[@data-type="widget"]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Связаться с оператором')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@class="UR_chatElement UR_chatElementRequired"]').send_keys('13')
    time.sleep(5)
    driver.find_element(By.XPATH, '//label[@class="UR_chatElement UR_chatScenarioFormSubmit"]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//textarea[@class="UR_chatElementRequired"]').send_keys('Как играть?')
    time.sleep(5)
    driver.find_element(By.XPATH, '(//button[@class="UR_chatScenarioFormSubmit"])[2]').click()
    time.sleep(10)
    for element, text in data:
        driver.find_element(By.XPATH, '(// textarea[@ placeholder="Написать ответ..."])[1]').send_keys(text)
        time.sleep(3)
        driver.find_element(By.XPATH, '//div[@class="UR_chatElement UR_chatSendButton"]').click()
        assert element.is_enabled(), f'Элемент {text} не кликабелен'
        assert element.is_displayed(), f'Элемент {text} не кликабелен'

    driver.quit()
    driver.close()
