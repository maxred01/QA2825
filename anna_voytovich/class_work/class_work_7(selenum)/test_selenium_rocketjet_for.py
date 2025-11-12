import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://superjet.rostsayt.ru/#')
    driver.maximize_window()
    time.sleep(3)
    locators = [
        (driver.find_element(By.XPATH, '(//nav//a)[1]//*[@alt=""]'), 'кнопка superjet', 'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH, '(//*[@id="navbarSupportedContent"]//ul//*[@aria-current="page"])[1]'),'кнопка преимущества',  'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH,"(//*[@type='button' and @role='presentation' and contains(concat(' ', normalize-space(@class), ' '), ' owl-next ')])[1]"),'стрелка вправо', 'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH,"(//*[@type='button' and @role='presentation' and contains(concat(' ', normalize-space(@class), ' '), ' owl-prev ')])[1]"), 'стрелка влево', 'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH, '(//header//li)[2]//*[@aria-current="page"]'), 'кнопка эффективность',  'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH, '(//header//ul//*[@aria-current="page"])[3]'), 'кнопка комплектация',  'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH, '(//*[@id="accordionExample"]//h2)[1]//*[@aria-expanded="false"]'),'кнопка стрелки вниз 1ая', 'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH, '(//*[@id="accordionExample"]//h2)[1]//*[@aria-expanded="false"]'),'кнопка стрелки вниз 1ая', 'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH, '(//nav//ul//*[@aria-current="page" and @href="#comforts"])[1]'),'кнопка комфорт',  'https://superjet.rostsayt.ru/#'),
        (driver.find_element(By.XPATH, '(//header//ul//*[@aria-current="page" and @href="#feedbacks"])[1]'),'кнопка купить в лизинг', 'https://superjet.rostsayt.ru/#'),
    ]
    driver.find_element(By.XPATH, '(//*[@id="navbarSupportedContent"]//ul//*[@aria-current="page"])[1]').click()
    assert driver.find_element(By.XPATH, "(//div[contains(concat(' ', normalize-space(@class), ' '), ' active ')]//*[@src='assets/images/slider/01.jpg' and @alt=""])[1]").is_enabled()
    driver.find_element(By.XPATH, "(//*[@type='button' and @role='presentation' and contains(concat(' ', normalize-space(@class), ' '), ' owl-next ')])[1]").click()




    for element, text, url in locators:
        element.click()
        assert driver.current_url == url, f'неверная ссылка {text}'
        assert element.is_enabled(), f'Элемент {text} не кликабелен'
        assert element.is_displayed(), f'Элемента {text} нет на экране'

        time.sleep(1)

    driver.execute_script('window.scrollBy(0, 500)')
    time.sleep(2)

    app_button = driver.find_element(By.XPATH, '//button[@class="feedback-btn"]')
    assert app_button.is_displayed(), 'Элемента нет на экране'
    assert app_button.is_enabled(), 'Элемент не кликабелен'
    assert app_button.text == 'Оставить заявку', f'Неверный текст. Получено {app_button.text}'
    app_button.click()

    field_name = driver.find_element(By.XPATH, )
    time.sleep(2)

    driver.quit()
    driver.close()