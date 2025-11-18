import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://demoqa.com/webtables')
    driver.maximize_window()

    add = driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]')
    add.click()
    assert add.is_enabled()

    first_name = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    first_name.send_keys('Anna')
    lastname = driver.find_element(By.XPATH, '//input[@id="lastName"]')
    lastname.send_keys('Voyt')
    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    email.send_keys('anna@gmail.com')
    age = driver.find_element(By.XPATH, '//input[@id="age"]')
    age.send_keys('10')
    salary = driver.find_element(By.XPATH, '//input[@id="salary"]')
    salary.send_keys('200')
    department = driver.find_element(By.XPATH, '//input[@id="department"]')
    department.send_keys('QA')
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[@id="submit"]').click()



    time.sleep(2)
    table_rows = driver.find_elements(By.XPATH, '//div[@class="rt-tr-group"]"]')
    assert len(table_rows) == 3, f"Ожидалось 3 строки, но найдено {len(table_rows)}"



