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
    submit = driver.find_element(By.XPATH,'//button[@id="submit"]')
    submit.click()

    time.sleep(2)

    table_rows = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]')

    empty_rows = driver.find_elements(By.XPATH, '//div[@class="rt-tr -padRow -even"]') + driver.find_elements(By.XPATH, '//div[@class="rt-tr -padRow -odd"]')
    filled_rows = len(table_rows) - len(empty_rows)

    assert filled_rows == 4, f"Ожидалось 4 строки, но найдено {len(table_rows)}"

    trash_1 = driver.find_element(By.XPATH, '//span[@id = "delete-record-1"]')
    trash_1.click()

    time.sleep(2)


    name_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[15]')
    assert name_cell.text == 'Anna', f'Неверный текст. Получено {name_cell}'
    lastname_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[16]')
    assert lastname_cell.text == 'Voyt', f'Неверный текст. Получен {lastname_cell}'
    age_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[17]')
    assert age_cell.text == '10', f'Неверное значение. Получено {age_cell}'
    email_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[18]')
    assert email_cell.text == 'anna@gmail.com', f'Неверный емаел. Получен {email_cell}'
    salary_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[19]')
    assert salary_cell.text == '200', f'Неверное значение. Получено {salary_cell}'
    department_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[20]')
    assert department_cell.text == 'QA', f'Неверный текст. Получено {department_cell}'

    edit = driver.find_element(By.XPATH, '//span[@id = "edit-record-4"]')
    edit.click()

    time.sleep(2)

    salary_edit = driver.find_element(By.XPATH,'//input[@id = "salary"]')
    salary_edit.clear()
    time.sleep(2)
    salary_edit.send_keys('100000')
    submit_edit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit_edit.click()
    time.sleep(3)


    assert salary_cell.text == '100000', f'Неверное значение. Получено {salary_cell}'