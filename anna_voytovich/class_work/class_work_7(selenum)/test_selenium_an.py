import time


from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://hoster.by/')
    driver.maximize_window()
    # driver.set_window_size(340, 500)
    driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[3]/div/div[1]/div[1]/span').click()
    element = driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div[1]/a[1]/span[1]')
    assert element.is_displayed(), 'Элемента нет на экране'
    assert element.is_enabled(), 'Элемент не кликабелен'
    assert element.text == 'Регистрация домена', f'Неверный текст. Получено {element.text}'
    driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[3]/div/div[1]/div[1]/span').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Введите домен или слово"]').send_keys('test')
    driver.find_element(By.XPATH, '//button[@class="m-button grey m-icon"]').click()
    time.sleep(3)
    # element_text = driver.find_element(By.XPATH, )
    # assert element_text.text == 'test.by', f'Неверный текст домена'
    driver.execute_script('window.scrollBy(0, 500)')




    driver.close()
    driver.quit()
