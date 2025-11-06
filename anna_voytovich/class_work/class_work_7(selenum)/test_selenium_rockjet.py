import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://superjet.rostsayt.ru/#')
    driver.maximize_window()

    advantages_button = driver.find_element(By.XPATH, '/html/body/header/div/nav/div/div/ul/li[1]/a')
    assert advantages_button.is_displayed(), 'Элемента нет на экране'
    assert advantages_button.is_enabled(), 'Элемент не кликабелен'
    assert advantages_button.text == 'ПРЕИМУЩЕСТВА', f'Неверный текст. Получено {advantages_button.text}'
    advantages_button.click()

    driver.execute_script('window.scrollBy(0, 11000)')
    time.sleep(2)

    app_button = driver.find_element(By.XPATH, '//button[@class="feedback-btn"]')
    app_button.click()

    time.sleep(3)
