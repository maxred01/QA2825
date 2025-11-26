from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# def test_trenager():
#     driver=webdriver.Chrome()
#     driver.get('https://demoqa.com/checkbox')
#
#     time.sleep(7)
#
#     driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button').click()
#     time.sleep(3)
#     driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
#
#     time.sleep(3)
#     driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]').click()

    # найти норм локатор
    #assert driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').is_selected()

# def test_button():
#     driver = webdriver.Chrome()
#     driver.get('https://demoqa.com/radio-button')
#     #element=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[2]/p/span')
#
#     time.sleep(7)
#
#     driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/input').click()
#     time.sleep(3)
#     assert driver.find_element(By.XPATH,'//*[@id="yesRadio"]').is_selected()
#     assert driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[2]/p/span')
#     assert element.text=='Yes'
#     assert driver.find_element(By.XPATH,'//*[@id="noRadio"]').is_enabled()

def test_menu():

    driver=webdriver.Chrome()
    driver.get('https://demoqa.com/webtables')
    time.sleep(3)

    driver.find_element(By.XPATH,'')




