import time
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/checkbox")

    driver.find_element(By.XPATH, '//button[@title="Toggle"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '(//button[@title="Toggle"])[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//label[@for="tree-node-commands"]').click()

    assert driver.find_element(By.ID, 'tree-node-commands').is_selected(), 'Элемент не выбран'

    driver.quit()
