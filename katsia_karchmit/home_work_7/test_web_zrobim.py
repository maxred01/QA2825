import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://zrobim.by/')
    driver.maximize_window()
    time.sleep(10)


    button = [
        (driver.find_element(By.XPATH, '//div[@class="menu-open__text"]'),"МЕНЮ"),
        (driver.find_element(By.XPATH, '//*[text()="Реализованные проекты"]'), "Реализованные проекты"),
        #(driver.find_element(By.XPATH, '//*[@data-more="#more-text" and text()="Читать больше"]'), "Читать больше"),
        #(driver.find_element(By.XPATH, '//span[@itemprop="name"][1]'), "Главная"),
        (driver.find_element(By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), ' menu-open__text ')]"), "МЕНЮ"),
        (driver.find_element(By.XPATH, '//a[text()="Контакты"]'), "Контакты"),
        (driver.find_element(By.XPATH, "//a[contains(concat(' ', normalize-space(@class), ' '), ' bold ') and text()='Предложение'][1]"), "Предложение"),
        (driver.find_element(By.XPATH, "//*[@alt='logo' and contains(concat(' ', normalize-space(@class), ' '), ' header__header-logo ')][1]"), "Логотип"),
        ]

    for element, text in button:
        element.click()
        time.sleep(20)
        assert element.is_displayed(), f'Элемент {text} отсутствует'
        assert element.is_enabled(), f'Элемент {text} не кликабелен'

    driver.close()
    driver.quit()
