import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/webtables')
    time.sleep(5)

    driver.execute_script('window.scrollBy(0, 200)')
    rows = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]')
    empty_rows = driver.find_elements(By.XPATH, '//div[@class="rt-tr -padRow -even"]') + driver.find_elements(By.XPATH,'//div[@class="rt-tr -padRow -odd"]')
    filled_rows = len(rows) - len(empty_rows)
    assert filled_rows == 3, f"В таблице заполнено {filled_rows} строки"

    add_button = driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]')
    add_button.click()
    time.sleep(3)

    first_name = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    first_name.send_keys('Anya')
    last_name = driver.find_element(By.XPATH, '//input[@id="lastName"]')
    last_name.send_keys('Beketova')
    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    email.send_keys('a_beketova@tester.by')
    age = driver.find_element(By.XPATH, '//input[@id="age"]')
    age.send_keys('17')
    salary = driver.find_element(By.XPATH, '//input[@id="salary"]')
    salary.send_keys('48000')
    department = driver.find_element(By.XPATH, '//input[@id="department"]')
    department.send_keys('Department of QA')
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()

    rows = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]')
    empty_rows = driver.find_elements(By.XPATH, '//div[@class="rt-tr -padRow -even"]') + driver.find_elements(By.XPATH,'//div[@class="rt-tr -padRow -odd"]')
    filled_rows = len(rows) - len(empty_rows)
    assert filled_rows == 4, f"В таблице заполнено {filled_rows} строки"

    delete_button = driver.find_element(By.XPATH, '//span[@id="delete-record-1"]')
    delete_button.click()

    cell_lastname = driver.find_element(By.XPATH, '(//*[@role="gridcell"])[16]')
    assert cell_lastname.text == 'Beketova', f'Текст в ячейке:{cell_lastname.text}'

    edit_button = driver.find_element(By.XPATH, '(//span[@id="edit-record-4"])')
    edit_button.click()
    edit_lastname = driver.find_element(By.XPATH, '//input[@id="lastName"]')
    edit_lastname.clear()
    edit_lastname.send_keys('Garbuzova')
    submit_edit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit_edit.click()
    assert cell_lastname.text == 'Garbuzova', f'Текст в ячейке: {cell_lastname.text}'

    driver.quit()