import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://zrobim.by/')
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/button/div[1]').click()
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/ul[2]/li[2]/a')
    assert element.is_displayed(), 'Элемента нет на экране'
    assert element.is_enabled(), 'Элемент не кликабелен'
    # assert element.text == 'Реализованные проекты', f'Неверный текст. Получено {element.text}'
    # driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[3]/div/div[1]/div[1]/span').click()


    #driver.execute_script('window.scrollBy()0, 500')

    time.sleep(4)
    driver.close()
    driver.quit()
