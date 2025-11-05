import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://tryhackme.com/')
    driver.maximize_window()
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[2]/div/div[1]/button').click()
    # driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[1]/nav[1]/ul/li[2]/button').click()
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[1]/nav[1]/ul/li[2]/div/div/a[1]/div')

    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[2]/div/div[1]/div/div/div[1]/div/input').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[2]/div/div[1]/div/div/div[1]/div/input').send_keys('test')
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[2]/div/div[1]/div/div/div[1]/div/input').send_keys(Keys.ENTER)
    element_text = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/main/div[2]/div/div/div/div[1]/div[2]/div[1]/input')
    time.sleep(3)
    assert element.text == 'test', f"Неверный текст. Получен {element_text.text}"
    # assert element.is_displayed(), 'Этот элемент отсутствует на экране'
    # assert element.is_enabled(), 'Этот элемент не кликабелен'
    # assert element.text == 'Challenges\nReinforce your learning', f"Неверный текст. Получено {element.text}"
    # driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[1]/nav[1]/ul/li[2]/button').click()
    # driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[2]/div/div[1]/button').click()
    # driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div/header/div/div[1]/nav[1]/ul/li[2]/button').click()

    # driver.execute_script('window.scrollBy(0, 1500)')
    time.sleep(3)

    driver.close()
    driver.quit()
