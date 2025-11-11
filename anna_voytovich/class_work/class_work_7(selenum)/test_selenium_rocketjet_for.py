import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://superjet.rostsayt.ru/#')
    driver.maximize_window()
    time.sleep(3)
    locators = [
        (driver.find_element(By.XPATH, '(//nav//a)[1]//*[@alt=""]'), 'кнопка superjet'),
        (driver.find_element(By.XPATH, '(//*[@id="navbarSupportedContent"]//ul//*[@aria-current="page"])[1]'), 'кнопка преимущества'),
        (driver.find_element(By.XPATH, "(//*[@type='button' and @role='presentation' and contains(concat(' ', normalize-space(@class), ' '), ' owl-next ')])[1]"), 'стрелка вправо'),
        (driver.find_element(By.XPATH, "(//*[@type='button' and @role='presentation' and contains(concat(' ', normalize-space(@class), ' '), ' owl-prev ')])[1]"), 'стрелка влево'),
        (driver.find_element(By.XPATH, '(//header//li)[2]//*[@aria-current="page"]'), 'кнопка эффективность'),
        (driver.find_element(By.XPATH, '(//header//ul//*[@aria-current="page"])[3]'), 'кнопка комплектация'),
        (driver.find_element(By.XPATH, '(//*[@id="accordionExample"]//h2)[1]//*[@aria-expanded="false"]'), 'кнопка стрелки вниз 1ая'),
        (driver.find_element(By.XPATH, '(//*[@id="accordionExample"]//h2)[1]//*[@aria-expanded="false"]'), 'кнопка стрелки вниз 1ая'),
        (driver.find_element(By.XPATH, '//*[@id="headingTwo"]//button[@aria-expanded="false"]'), 'кнопка стрелки вниз 2ая'),
        (driver.find_element(By.XPATH, '//*[@id="headingTwo"]//button[@aria-expanded="false"]'), 'кнопка стрелки вниз 2ая'),
        (driver.find_element(By.XPATH, '//*[@id="accordionExample"]//button[@aria-controls="collapseThree"]'), 'кнопка стрелка вниз 3я'),
        (driver.find_element(By.XPATH, '//*[@id="accordionExample"]//button[@aria-controls="collapseThree"]'), 'кнопка стрелка вниз 3я'),
        (driver.find_element(By.XPATH, '(//nav//ul//*[@aria-current="page" and @href="#comforts"])[1]'), 'кнопка комфорт'),
        (driver.find_element(By.XPATH, '(//header//ul//*[@aria-current="page" and @href="#feedbacks"])[1]'), 'кнопка купить в лизинг'),
            ]

    for element, text in locators:
        element.click()
        assert element.is_enabled(), f'Элемент {text} не кликабелен'
        assert element.is_displayed(), f'Элемент {text} не кликабелен'

        time.sleep(1)

    driver.quit()
    driver.close()