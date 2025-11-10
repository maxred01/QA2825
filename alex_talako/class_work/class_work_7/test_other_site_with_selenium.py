import time
from os import times_result
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selenium_again():
    driver = webdriver.Chrome()
    driver.get('https://tryhackme.com/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="sc-banner"]//button')))

    driver.close()
    driver.quit()