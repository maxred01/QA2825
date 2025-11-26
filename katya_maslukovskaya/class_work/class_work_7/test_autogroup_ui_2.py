import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selenium_autogroup():
    driver=webdriver.Chrome()
    driver.get('https://autogroup.by/')
    #неявное ожидание
    driver.implicitly_wait(10)
    #явное ожидание
    #wait=WebDriverWait(driver,10)
    button=driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[2]")
    wait.until(EC.visibility_of_e)
    if button.is_enabled():
        button.click()
    else:
        print('не работает')
    driver.quit()
    driver.close()

def test_autogroup_wait():
    driver=webdriver.Chrome()
    driver.get('https://autogroup.by/')
    driver.find_element((By.XPATH,"((//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[1]")).click()
    time.sleep(5)
