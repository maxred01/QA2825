import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://demoqa.com/radio-button')
    driver.maximize_window()

    driver.find_element(By.XPATH, '//label[@for="yesRadio"]').click()
    assert driver.find_element(By.XPATH, '//label[@for="yesRadio"]').is_enabled()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//span[@class="text-success"]').text == 'Yes', f'данный текст не отображается'
    assert not driver.find_element(By.XPATH, '(//input[@type="radio" and @id="noRadio" and @name="like"])[1]').is_enabled()



    driver.quit()
    driver.close()

