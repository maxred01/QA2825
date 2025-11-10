import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_selenium():
    driver=webdriver.Chrome()

    driver.get('https://autogroup.by/')
    #driver.maximize_window()

#поиск элемента и клик на него
    driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[2]").click()

#поиск элемента
    element=driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' menu-item ')])[3]")
    assert element.is_displayed, 'Элемента нет'
    assert element.is_enabled, 'Элемент не кликабелен'

#проверка текста внутри объекта
    assert element.text=='Доставка', f'Неверный текст. Получено {element.text}'

    driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' menu-item ')])[2]").click()
    driver.find_element(By.XPATH,'(//header//a)[8]').click()

#вводим цену от
    driver.find_element(By.XPATH,'//*[@name="MIN"]').click()
    driver.find_element(By.XPATH,'//*[@name="MIN"]').send_keys('20000')
    driver.find_element(By.XPATH,'//*[@name="MIN"]').send_keys(Keys.ENTER)

#вводим цену до
    driver.find_element(By.XPATH,'//*[@name="MAX"]').click()
    driver.find_element(By.XPATH,'//*[@name="MAX"]').send_keys('70000')
    driver.find_element(By.XPATH,'//*[@name="MAX"]').send_keys(Keys.ENTER)

#выбираем марку
    driver.find_element(By.XPATH,'//*[@id="view-MARK"]').click()
    driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' new-select__item ')])[4]").click()

#выбираем модель
    driver.find_element(By.XPATH,'//*[@id="view-MODEL"]').click()
    driver.find_element(By.XPATH,'//*[@id="MODEL"]/*[4]').click()

#выбираем кузов
    driver.find_element(By.XPATH,'//*[@id="view-CAR_BODY"]').click()
    driver.find_element(By.XPATH,"//*[@id=\"CAR_BODY\"]//*[contains(concat(' ', normalize-space(@class), ' '), ' new-select__item ')]").click()

#поиск
    driver.find_element(By.XPATH,'//*[@type="submit"]').click()

#поиск выдачи
    # element_one=driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' catalog-item__name ')])[2]")
    # assert element_one.is_displayed, 'Элемента нет'














    #driver.find_element(By.XPATH'')

    #driver.execute_script('window.scrollBY(0,500)')


    time.sleep(3)
    driver.close()
    driver.quit()
