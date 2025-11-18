import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_selenium():

    driver = webdriver.Chrome()
    driver.get('https://autogroup.by/catalog-usa/')
    driver.maximize_window()

    driver.find_element(By.XPATH, '//input[@id = MIN]').send_keys('10000')
    driver.find_element(By.XPATH, '//input[@id = MAX]').send_keys('15000')
    driver.find_element(By.XPATH,"//button[@type='submit']").click()