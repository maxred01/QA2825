import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/radio-button')
    time.sleep(3)
    driver.find_element(By.XPATH, '//label[@for="yesRadio"]').click()
    assert driver.find_element(By.XPATH, '//label[@for="yesRadio"]').is_enabled()
    assert driver.find_element(By.XPATH, '//span[@class="text-success"]').text == 'Yes', 'Yes отсутствует'
    assert not driver.find_element(By.XPATH, '(//input[@type="radio" and @id="noRadio" and @name="like"])[1]').is_enabled()



    driver.quit()
    driver.close()