import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://zrobim.by/')
    driver.maximize_window()
    time.sleep(3)
    #проверка кнопки "меню"
    driver.find_element(By.XPATH, '//div[@class="menu-open__text"]').click()
    #проверка кнопки "Реализованные проекты"
    element = driver.find_element(By.XPATH, '//*[text()="Реализованные проекты"]')
    assert element.is_displayed(), 'Элемента нет на экране'
    assert element.is_enabled(), 'Элемент не кликабелен'
    assert element.text == 'РЕАЛИЗОВАННЫЕ ПРОЕКТЫ', f'Неверный текст. Получено {element.text}'
    #проверка скролинга страницы
    driver.find_element(By.XPATH, '//a[contains(text(),"Реализованные проекты") and //div[@id="menu"]]').click()
    driver.execute_script('window.scrollBy(0,1500)')
    time.sleep(3)
    driver.find_element(By.XPATH, "(//*[contains(concat(' ', normalize-space(@class), ' '), ' category__item-title ') and text()='LEV APARTMENT'])[1]").click()
    time.sleep(3)
    driver.execute_script('window.scrollBy(0,3000)')
    time.sleep(3)
    #проверка запуска видео
    # video_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-caption='LEV APARTMENT' and contains(concat(' ', normalize-space(@class), ' '), ' youtube__item ')]")))
    # driver.execute_script("arguments[0].click()", video_element)
    # time.sleep(15)
    # video_element.click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//button[@class='ytp-play-button ytp-button']").click()
    # driver.find_element(By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), ' fancybox-slide ')]").click()

    # проверка кнопки "консультант"
    driver.find_element(By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), ' header__header ')]//button").click()
    time.sleep(8)
    # проверка заполнения поля
    driver.find_element(By.XPATH, '(//*[@id="feedback-name" and @name="name" and @type="text"])[2]').send_keys('Karl')
    driver.find_element(By.XPATH, '//*[@fill="none"][1]').click()

    #проверка кнопки вакансии
    driver.find_element(By.XPATH, '//div[@class="menu-open__text"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//a[contains(text(),"Вакансии") and //div[@id="menu"]]').click()
    time.sleep(6)
    #проверка заполнения поля
    driver.find_element(By.XPATH, '//input[@name="name"][1]').send_keys('Karl')
    time.sleep(3)

    #проверка кнопки контакты
    driver.find_element(By.XPATH, '//div[@class="menu-open__text"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//a[text()="Контакты"]').click()
    time.sleep(4)
    driver.execute_script('window.scrollBy(0,3000)')
    time.sleep(4)

    #проверка заполнения поля
    driver.find_element(By.XPATH, '//*[@id="feedback-comment"]').send_keys('Work in your company.')
    time.sleep(4)
    driver.execute_script('window.scrollBy(0,-3000)')
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@alt='logo' and contains(concat(' ', normalize-space(@class), ' '), ' header__header-logo ')][1]").click()
    time.sleep(6)
    driver.close()
    driver.quit()