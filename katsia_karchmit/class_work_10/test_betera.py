import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://pm.by/ru/')
    driver.maximize_window()
    time.sleep(10)

    driver.find_element(By.XPATH,"(//div[@id='cookiescript_accept'])[1]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="modal-root"]//i').click()
    time.sleep(10)
    driver.find_element(By.XPATH, "(//header//button[text()='Ок'])[1]").click()
    time.sleep(10)

    driver.close()
    driver.quit()

