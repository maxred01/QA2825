import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import allure
@allure.title('UI тесты')
@allure.epic('Тест меню на главной странице')
@allure.story('Позитивные тесты')
@allure.feature('Консультация')

def test_selenium():
    with allure.step('Подготовка тестовых данных'):
        driver=webdriver.Chrome()

        driver.get('https://autogroup.by/')
        time.sleep(3)
    #driver.maximize_window()

#поиск элемента и клик на него
    with allure.step('Поиск элемента и клик'):
        driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[2]").click()

#поиск элемента
    with allure.step('Поиск элемента'):
        element=driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' menu-item ')])[3]")
        assert element.is_displayed, 'Элемента нет'
        assert element.is_enabled, 'Элемент не кликабелен'

#проверка текста внутри объекта
    with allure.step('Поиск элемента и проверка текста в нем'):
        assert element.text=='Доставка', f'Неверный текст. Получено {element.text}'

    with allure.step('Поиск элемента и клик'):
        driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' menu-item ')])[2]").click()
        driver.find_element(By.XPATH,'(//header//a)[8]').click()
        time.sleep(5)

#вводим цену от
    with allure.step('Ввод цены от'):
        driver.find_element(By.XPATH,'//*[@name="MIN"]').click()
        driver.find_element(By.XPATH,'//*[@name="MIN"]').send_keys('20000')
        driver.find_element(By.XPATH,'//*[@name="MIN"]').send_keys(Keys.ENTER)
        time.sleep(3)

#вводим цену до
    with allure.step('Ввод цены до'):
        driver.find_element(By.XPATH,'//*[@name="MAX"]').click()
        driver.find_element(By.XPATH,'//*[@name="MAX"]').send_keys('70000')
        driver.find_element(By.XPATH,'//*[@name="MAX"]').send_keys(Keys.ENTER)
        time.sleep(3)

#выбираем марку
    with allure.step('Выбор в поле марка'):
        driver.find_element(By.XPATH,'//*[@id="view-MARK"]').click()
        driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' new-select__item ')])[4]").click()
        time.sleep(5)

#выбираем модель
    with allure.step('Выбор в поле модель'):
        driver.find_element(By.XPATH,'//*[@id="view-MODEL"]').click()
        driver.find_element(By.XPATH,'//*[@id="MODEL"]/*[4]').click()
        time.sleep(5)

#выбираем кузов
    with allure.step('Выбор в поле кузов'):
        driver.find_element(By.XPATH,'//*[@id="view-CAR_BODY"]').click()
        driver.find_element(By.XPATH,"//*[@id=\"CAR_BODY\"]//*[contains(concat(' ', normalize-space(@class), ' '), ' new-select__item ')]").click()
        time.sleep(5)

#поиск
    with allure.step('Кнопка применить'):
        driver.find_element(By.XPATH,'//*[@type="submit"]').click()
        time.sleep(5)

#поиск выдачи
    element_one=driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' main_page-item__name ')])[2]")
    assert element_one.is_displayed, 'Элемента нет'

    driver.close()
    driver.quit()
