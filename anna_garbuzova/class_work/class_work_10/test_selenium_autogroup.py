import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://autogroup.by/catalog-usa/')

    driver.find_element(By.XPATH, '').click()

    driver.quit()
    driver.close()