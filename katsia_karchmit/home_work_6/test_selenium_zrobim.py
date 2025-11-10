import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://zrobim.by/')
    driver.maximize_window()
    time.sleep(4)
    #проверка кнопки "меню"
    driver.find_element(By.XPATH, '//div[@class="menu-open__text"]').click()
    # #проверка кнопки "Реализованные проекты"
    # element = driver.find_element(By.XPATH, '//*[text()="Реализованные проекты"]')
    # assert element.is_displayed(), 'Элемента нет на экране'
    # assert element.is_enabled(), 'Элемент не кликабелен'
    # assert element.text == 'РЕАЛИЗОВАННЫЕ ПРОЕКТЫ', f'Неверный текст. Получено {element.text}'
    #
    #
    # #проверка скролинга страницы
    # driver.find_element(By.XPATH, '//a[contains(text(),"Реализованные проекты") and //div[@id="menu"]]').click()
    # driver.execute_script('window.scrollBy(0,2000)')
    # time.sleep(6)
    # проверка кнопки "консультант"
    #driver.find_element(By.XPATH, '//button[contains(text(),"консультант")]').click()
    #time.sleep(6)
    # проверка заполнения поля
    #driver.find_element(By.XPATH, '//*[@id="feedback-name"]').send_keys('Karl')

    #проверка кнопки вакансии
    # driver.find_element(By.XPATH, '//a[contains(text(),"Вакансии") and //div[@id="menu"]]').click()
    # time.sleep(6)
    # #проверка заполнения поля
    # driver.find_element(By.XPATH, '//input[@name="name"][1]').send_keys('Karl')

    #проверка кнопки контакты
    driver.find_element(By.XPATH, '//a[text()="Контакты"]').click()
    time.sleep(2)
    driver.execute_script('window.scrollBy(0,2000)')
    time.sleep(2)
    # проверка заполнения поля
    driver.find_element(By.XPATH, '//*[@id="feedback-comment"]').send_keys('Work in your company.')

    time.sleep(6)
    driver.close()
    driver.quit()