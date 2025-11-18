import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/checkbox')
    driver.find_element(By.XPATH, '(//button[@aria-label="Expand all"])[1]').click()
    driver.find_element(By.XPATH,'(//*[@for="tree-node-commands"]//*[local-name() = "svg"][@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//input[@id="tree-node-commands" and @type="checkbox"]').is_selected()
    driver.find_element(By.XPATH,'(//*[@for="tree-node-workspace"]//*[local-name() = "svg"][@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//input[@id="tree-node-workspace" and @type="checkbox"]').is_selected()
    driver.find_element(By.XPATH, '(//button[@aria-label="Toggle"])[6]').click()
    driver.find_element(By.XPATH,'(//*[@for="tree-node-excelFile"]//*[local-name() = "svg"][@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//input[@id="tree-node-excelFile" and @type="checkbox"]').is_selected()

    driver.quit()
    driver.close()
