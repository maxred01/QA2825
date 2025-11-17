import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_with_selenium():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    time.sleep(2)
    driver.find_element(By.XPATH, '(//*[@id="app"]//div)[7]').click()
    time.sleep(2)
    # driver.find_element(By.XPATH, '(//*[@id="app"]//li)[2]').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@aria-label="Toggle"]//*[@stroke="currentColor"]').click()
    # driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[2]//*[@stroke="currentColor"]').click()
    # driver.find_element(By.XPATH, '((//*[@id="app"]//label)[3]//*[@stroke="currentColor"])[1]').click()
    # assert driver.find_element(By.XPATH, '//*[@id = "tree-node-notes" and @type ="checkbox"]').is_selected(), 'Элемент не выбран '
    # time.sleep(3)
    # driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[3]//*[@stroke="currentColor"]').click()
    # driver.find_element(By.XPATH, '((//*[@id="tree-node"]//label)[7]//*[@stroke="currentColor"])[1]').click()
    # assert driver.find_element(By.XPATH, '//*[@id = "tree-node-notes" and @type ="checkbox"]').is_selected(), 'Элемент не выбран'
    # time.sleep(3)
    # driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[6]//*[@stroke="currentColor"]').click()
    # driver.find_element(By.XPATH, '((//*[@id="tree-node"]//label)[9]//*[@stroke="currentColor"])[1]').click()
    # assert driver.find_element(By.XPATH, '//*[@id = "tree-node-notes" and @type ="checkbox"]').is_selected(), 'Элемент не выбран'
    # time.sleep(2)
    # driver.find_element(By.XPATH, '(//*[@id="app"]//li)[3]').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '(//*[@id="app"]//label)[1]').click()
    # time.sleep(2)
    # assert driver.find_element(By.XPATH, '//span[@class="text-success"]').is_enabled(), 'Элемент не выбран'
    # time.sleep(2)
    # assert driver.find_element(By.XPATH, '//span[@class="text-success"]').text == 'Yes', f"Неверный текст"
    # time.sleep(2)
    # assert not driver.find_element(By.XPATH, '(//input[@type="radio" and @id="noRadio" and @name="like"])[1]').is_enabled(), 'Элемент можно выбрать'


    driver.find_element(By.XPATH, '(//*[@id="app"]//ul)[1]/*[3]').click()
    time.sleep(2)
    rows = driver.find_elements(By.XPATH, '//div[@class="rt-tr -odd" and @role="row"]')
    row_count = len(rows)
    assert len(rows) == 3
    driver.close()
    driver.quit()
