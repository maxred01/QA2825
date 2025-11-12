import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL_const = 'https://zrobim.by/'
def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://zrobim.by/')
    driver.maximize_window()
    time.sleep(10)


    button = [
        (driver.find_element(By.XPATH, '//a[text()="О студии"]'), "О студии",'team.html'),
        (driver.find_element(By.XPATH, '//*[text()="Реализованные проекты"]'), "Реализованные проекты",'realzavanyiya-praektyi.html'),
        (driver.find_element(By.XPATH, '//a[text()="Мастер-классы"]'), "Мастер-классы", 'education.html'),
        (driver.find_element(By.XPATH, '//a[text()="Контакты"]'), "Контакты",),
        ]

    for element, text, url in button:
        driver.find_element(By.XPATH, '//div[@class="menu-open__text"]').click()
        time.sleep(5)
        if element.is_enabled():
            time.sleep(5)
            element.click()
            assert driver.current_url == URL_const+url, f'Неверная ссылка {text}'


    driver.close()
    driver.quit()
