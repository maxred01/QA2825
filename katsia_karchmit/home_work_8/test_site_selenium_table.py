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
    Elements = driver.find_element(By.XPATH, '(//*[@id="app"]//div)[7]')
    Elements.click()
    time.sleep(2)
    Web_Tables = driver.find_element(By.XPATH, '(//*[@id="app"]//span[text()="Web Tables"])[1]')
    Web_Tables.click()
    assert Web_Tables.is_enabled()
    time.sleep(2)
    # Считаем количество строк ДО добавления
    rows_before = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']//div[@role='row' and .//div[@role='gridcell' and text()!='']]")
    print(f"Строк ДО добавления: {len(rows_before)}")
    Add = driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]')
    Add.click()
    assert Add.is_enabled()
    time.sleep(2)
    First_Name = driver.find_element(By.XPATH, '//*[@placeholder="First Name"]')
    First_Name.send_keys('Karl')
    time.sleep(2)
    Last_Name = driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]')
    Last_Name.send_keys('Franz')
    Email = driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]')
    Email.send_keys('Karl_Franz@gmail.com')
    Age = driver.find_element(By.XPATH, '//*[@placeholder="Age"]')
    Age.send_keys('28')
    Salary = driver.find_element(By.XPATH, '//*[@placeholder="Salary"]')
    Salary.send_keys('2800')
    Department = driver.find_element(By.XPATH, '//*[@placeholder="Department"]')
    Department.send_keys('IT')
    Submit = driver.find_element(By.XPATH, '(//*[@aria-modal="true"]//button[@id="submit"])[1]')
    Submit.click()
    time.sleep(5)
    element_Last_Name = driver.find_element(By.XPATH, '((//*[@role="rowgroup"])[4]//*[@role="gridcell"])[2]')
    assert element_Last_Name.is_displayed(), 'Элемента нет на экране'
    assert element_Last_Name.text == 'Franz', f'Неверный текст. Получено {element_Last_Name.text}'

    table_rows = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']//div[@role='row' and .//div[@role='gridcell' and text()!='']]")
    actual_row_count = len(table_rows)

    expected_row_count = 4
    assert actual_row_count == expected_row_count, \
        f"Ошибка: Ожидалось {expected_row_count} строк, но найдено {actual_row_count}."

    print(f"Проверка успешна: В таблице ровно {actual_row_count} строк.")

    delete_first_line = driver.find_element(By.XPATH, '//span[@id="delete-record-1"]')
    delete_first_line.click()
    time.sleep(3)

    edit_button = driver.find_element(By.XPATH, '//span[@id ="edit-record-4"]')
    edit_button.click()
    time.sleep(2)

    Salary_edit = driver.find_element(By.XPATH, '//*[@placeholder="Salary"]')
    Salary_edit.clear()
    Salary_edit.send_keys('4500')
    Submit_edit = driver.find_element(By.XPATH, '(//*[@aria-modal="true"]//button[@id="submit"])[1]')
    Submit_edit.click()
    time.sleep(2)

    Salary = driver.find_element(By.XPATH, '(//*[@role="row"])[4]/*[5]')
    assert Salary.text == '4500', f"Неверный текст. Получено {Salary.text}"

    driver.close()
    driver.quit()