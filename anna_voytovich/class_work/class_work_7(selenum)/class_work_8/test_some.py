import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as  EC
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()
    driver.get('https://zrobim.by/')
    driver.implicitly_wait(10)
    # consult_button = driver.find_element(By.XPATH, "(//*[@data-modal-open='#modal-feedback' and @onclick='ym(62748322,'reachGoal','konsult'); return true;'])[2]")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(By.XPATH, '')


    driver.quit()
    driver.close()