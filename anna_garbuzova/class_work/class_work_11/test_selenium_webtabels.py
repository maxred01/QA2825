import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/webtables')
    time.sleep(10)
    rows = driver.find_element(By.XPATH, '').click()
    # assert driver.find_element(By.XPATH, '//*[@id="yesRadio"]').is_selected()
    # driver.find_element(By.XPATH, '//span[@class="text-success"]').click()
    time.sleep(5)

    #assert driver.find_element(By.XPATH, '//*[@id="tree-node-notes"]').is_selected()

    driver.quit()
    driver.close()