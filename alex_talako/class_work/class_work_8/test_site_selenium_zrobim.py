import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_CONST = 'https://zrobim.by/'

def test_selenium_site():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://zrobim.by/')
    time.sleep(8)
    data =[
        (driver.find_element(By.XPATH, '//*[@href="/team.html"]'), 'кнопка о студии', 'team.html'),
        (driver.find_element(By.XPATH, '//*[@href = "/realzavanyiya-praektyi.html"]'), 'кнопка реализованные проекты', 'realzavanyiya-praektyi.html'),
        (driver.find_element(By.XPATH, '//*[@href="/arkhitektura/proektirovanie-chastnyh-domov.html"]'), 'кнопка частные дома', 'arkhitektura/proektirovanie-chastnyh-domov.html'),
    ]

    for element, text, url in data:
        driver.find_element(By.XPATH, '//*[@class="menu-open"]').click()
        time.sleep(3)
        element.click
        time.sleep(2)
        assert driver.current_url == URL_CONST + url, f'Неверная ссылка {text}'

    driver.close()
    driver.quit()