import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_with_selenium():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    time.sleep(3)
    driver.execute_script('window.scrollBy(0, 500)')
    driver.find_element(By.XPATH, '(//*[@id="app"]//div)[7]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '(//*[@id="app"]//li)[2]').click()
    time.sleep(3)
    driver.execute_script('window.scrollBy(0, 500)')
    driver.find_element(By.XPATH, '//*[@aria-label="Toggle"]//*[@stroke="currentColor"]').click()
    driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[2]').click()
    driver.find_element(By.XPATH, '((//*[@id="app"]//label)[3]//*[@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//*[@id = "tree-node-notes" and @type ="checkbox"]').is_selected(), 'Элемент не выбран'
    driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[3]//*[@stroke="currentColor"]').click()
    driver.find_element(By.XPATH, '((//*[@id="tree-node"]//label)[7]//*[@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//*[@id = "tree-node-notes" and @type ="checkbox"]').is_selected(), 'Элемент не выбран'
    driver.find_element(By.XPATH, '(//*[@aria-label="Toggle"])[6]//*[@stroke="currentColor"]').click()
    driver.find_element(By.XPATH, '((//*[@id="tree-node"]//label)[9]//*[@stroke="currentColor"])[1]').click()
    assert driver.find_element(By.XPATH, '//*[@id = "tree-node-notes" and @type ="checkbox"]').is_selected(), 'Элемент не выбран'
    time.sleep(2)
    driver.find_element(By.XPATH, '(//*[@id="app"]//li)[3]').click()
    time.sleep(2)
    driver.execute_script('window.scrollBy(0, 500)')
    driver.find_element(By.XPATH, '(//*[@id="app"]//label)[1]').click()
    assert driver.find_element(By.XPATH, '//span[@class="text-success"]').is_enabled(), 'Элемент не выбран'
    assert driver.find_element(By.XPATH, '//span[@class="text-success"]').text == 'Yes', f"Неверный текст"
    assert not driver.find_element(By.XPATH, '(//input[@type="radio" and @id="noRadio" and @name="like"])[1]').is_enabled(), 'Элемент можно выбрать'

    driver.find_element(By.XPATH, '(//*[@id="app"]//li)[4]').click()
    driver.execute_script('window.scrollBy(0, 200)')
    add = driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]')
    add.click()
    assert add.is_enabled()

    first_name = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    first_name.send_keys('Alex')
    lastname = driver.find_element(By.XPATH, '//input[@id="lastName"]')
    lastname.send_keys('Talako')
    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    email.send_keys('talako@gmail.com')
    age = driver.find_element(By.XPATH, '//input[@id="age"]')
    age.send_keys('11')
    salary = driver.find_element(By.XPATH, '//input[@id="salary"]')
    salary.send_keys('10000')
    department = driver.find_element(By.XPATH, '//input[@id="department"]')
    department.send_keys('QAmonster')
    time.sleep(1)
    submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit.click()
    time.sleep(2)

    table_rows = driver.find_elements(By.XPATH, '//div[@role="rowgroup"]')
    empty_rows = driver.find_elements(By.XPATH, '//div[@class="rt-tr -padRow -even"]') + driver.find_elements(By.XPATH,'//div[@class="rt-tr -padRow -odd"]')
    filled_rows = len(table_rows) - len(empty_rows)

    assert filled_rows == 4, f"Ожидалось 4 строки, но найдено {len(table_rows)}"
    time.sleep(3)

    delete_first_line = driver.find_element(By.XPATH, '//span[@id="delete-record-1"]')
    delete_first_line.click()
    time.sleep(3)

    first_name_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[15]')
    assert first_name_cell.text == 'Alex', f"Неверный текст. Получено {first_name_cell.text}"

    lastname_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[16]')
    assert lastname_cell.text == 'Talako', f"Неверный текст. Получено {lastname_cell.text}"

    age_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[17]')
    assert age_cell.text == '11', f"Неверное значение. Получено {age_cell.text}"

    email_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[18]')
    assert email_cell.text == 'talako@gmail.com', f"Неверный текст. Получено {email_cell.text}"

    salary_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[19]')
    assert salary_cell.text == '10000', f"Неверное значение. Получено {salary_cell.text}"

    department_cell = driver.find_element(By.XPATH, '(//div[@role="gridcell"])[20]')
    assert department_cell.text == 'QAmonster', f"Неверный текс. Получено {department_cell.text}"

    edit_button = driver.find_element(By.XPATH, '//span[@id ="edit-record-4"]')
    edit_button.click()
    time.sleep(2)

    department_edit = driver.find_element(By.XPATH, '//input[@id="department"]')
    department_edit.clear()
    department_edit.send_keys('Министр не ваших дел')
    submit_edit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit_edit.click()
    time.sleep(2)

    assert department_cell.text == 'Министр не ваших дел', f"Неверный текст. Получено {department_cell.text}"

    driver.close()
    driver.quit()
