import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_selenium_with_cycle():
    driver = webdriver.Chrome()
    driver.get('https://tryhackme.com/')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, '//button[@class="sc-jEACwC hnVovF sc-gqteRq ctqrBQ"]').click()
    data = [
        (driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Learn page"]'), 'Learn'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Practice"]'),'Practice'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Compete"]'),'Compete'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Education"]'),'Education'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Business page"]'),'Business'),
        (driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Pricing page"]'),'Pricing'),
        (driver.find_element(By.XPATH, '(//*[@data-link="outlined"])[2]'),'Log In'),
        (driver.find_element(By.XPATH, '//*[@data-link="join"]'),'Join for FREE'),
        ]

    for element, text in data:
        element.click()
        time.sleep(3)
        assert element.is_displayed(), f'Элемент {text} отсутствует'
        assert element.is_enabled(), f'Элемент {text} не кликабелен'


    driver.close()
    driver.quit()