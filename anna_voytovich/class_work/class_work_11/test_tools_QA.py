import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://demoqa.com/checkbox')
    driver.maximize_window()

    driver.find_element(By.XPATH, '(//button[@aria-label="Toggle"])[1]').click()
    driver.find_element(By.XPATH, '(//button[@aria-label="Toggle"])[2]').click()
    driver.find_element(By.XPATH, '(//button[@aria-label="Toggle"])[3]').click()
    driver.find_element(By.XPATH, '(//*[@for="tree-node-commands"]//*[local-name() = "svg"][@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//input[@id="tree-node-commands" and @type="checkbox"]').is_selected()

    driver.find_element(By.XPATH, '(//*[@for="tree-node-workspace"]//*[local-name() = "svg"][@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//input[@id="tree-node-workspace" and @type="checkbox"]').is_selected()

    driver.execute_script('window.scrollBy(0, 200)')
    time.sleep(1)
    driver.find_element(By.XPATH,'(//button[@aria-label="Toggle"])[6]').click()
    driver.find_element(By.XPATH, '(//*[@for="tree-node-excelFile"]//*[local-name() = "svg"][@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//input[@id="tree-node-excelFile" and @type="checkbox"]').is_selected()



    time.sleep(1)