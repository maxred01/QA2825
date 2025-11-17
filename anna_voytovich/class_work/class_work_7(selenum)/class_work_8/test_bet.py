import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as  EC
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    data = [
        'как играть?',
        'ау',
        'что здесь нажимать?',
        'вы здесь?',
        'ответьте'
    ]
    driver = webdriver.Chrome()
    driver.get('https://pm.by/ru/')
    time.sleep(10)
    driver.find_element(By.XPATH, "//*[@id='modal-root']//i[contains(concat(' ', normalize-space(@class), ' '), ' digi_icon-close ')]").click()
    driver.find_element(By.XPATH, "(//*[@id='cookiescript_accept' and @role='button'])[1]").click()
    # driver.find_element(By.XPATH, "(//header//button[contains(concat(' ', normalize-space(@class), ' '), ' missions-tooltip__button ')])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@data-type='widget' and contains(concat(' ', normalize-space(@class), ' '), ' UR_chatElement ')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//*[@type='button' and text()='Связаться с оператором'])[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@name="property_263" and @maxlength="255"]').send_keys('71')
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[contains(concat(' ', normalize-space(@class), ' '), ' UR_chatElement ') and contains(concat(' ', normalize-space(@class), ' '), ' UR_chatScenarioFormSubmit ')])[1]").click()
    time.sleep(6)
    for text in data:
        driver.find_element(By.XPATH, "//*[local-name() = 'textarea'][@name="" and contains(concat(' ', normalize-space(@class), ' '), ' UR_chatElementRequired ')]").send_keys(text)
        time.sleep(5)
        driver.find_element(By.XPATH,"(//button[@type='button' and contains(concat(' ', normalize-space(@class), ' '), ' UR_chatScenarioFormSubmit ')])[2]").click()


    driver.quit()
    driver.close()