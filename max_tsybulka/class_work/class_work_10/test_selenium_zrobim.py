import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL_CONST = 'https://zrobim.by/'


def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://zrobim.by/')
    time.sleep(10)
    data = [
        (driver.find_element(By.XPATH, '//a[@href="/team.html"]'), 'кнопка "О студии"', 'team.html'),
        (driver.find_element(By.XPATH, "//a[contains(text(), 'Реализованные проекты')]"), 'кнопка "Реализованные проекты"', 'realzavanyiya-praektyi.html'),
        (driver.find_element(By.XPATH, '//a[@href="/arkhitektura/proektirovanie-chastnyh-domov.html"]'), 'кнопка "Частные дома"', 'arkhitektura/proektirovanie-chastnyh-domov.html'),

            ]
    for element, text, url in data:
        driver.find_element(By.XPATH, '//div[@class="menu-open__text"]').click()
        time.sleep(2)
        if element.is_enabled():
            time.sleep(1)
            element.click()
            assert driver.current_url == URL_CONST + url, f'Нверная ссылка {text}'

    driver.quit()
    driver.close()
