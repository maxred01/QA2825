import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def test_selenium():
#     driver = webdriver.Chrome()
#     driver.get('https://zelgavan.by/')
#     driver.implicitly_wait(10)
#     wait = WebDriverWait(driver, 10)
#
#     wait.until(EC.visibility_of_element_located((By.XPATH,"(//*[@href='/immovables' and contains(concat(' ', normalize-space(@class), ' '), ' b-nav__item ')])[2]"))).click()
#
#     driver.quit()

def test_selenium():
    driver = webdriver.Chrome()
    driver.get('https://pm.by/ru/')

    time.sleep(10)
    driver.find_element(By.ID, '#login').click()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH,"(//*[@href='/immovables' and contains(concat(' ', normalize-space(@class), ' '), ' b-nav__item ')])[2]"))).click()

    driver.quit()