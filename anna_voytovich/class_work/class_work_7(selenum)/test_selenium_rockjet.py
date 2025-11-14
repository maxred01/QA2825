import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()

    driver.get('https://superjet.rostsayt.ru/#')
    driver.maximize_window()

    superjet_header = driver.find_element(By.XPATH, '(//nav//a)[1]//*[@alt=""]')
    assert superjet_header.is_displayed(), 'Элемента нет на экране'
    assert superjet_header.is_enabled(), 'Элемент не кликабелен'
    superjet_header.click()


    advantages_header = driver.find_element(By.XPATH, '(//*[@id="navbarSupportedContent"]//ul//*[@aria-current="page"])[1]')
    assert advantages_header.is_displayed(), 'Элемента нет на экране'
    assert advantages_header.is_enabled(), 'Элемент не кликабелен'
    assert advantages_header.text == 'ПРЕИМУЩЕСТВА', f'Неверный текст. Получено {advantages_header.text}'
    advantages_header.click()
    time.sleep(1)
    assert driver.find_element(By.XPATH,'//div[@class="owl-item active center"]//img[@src="assets/images/slider/01.jpg"]').is_displayed()
    driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH,'//div[@class="owl-item active center"]//img[@src="assets/images/slider/02.jpg"]').is_displayed()
    driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH,'//div[@class="owl-item active center"]//img[@src="assets/images/slider/03.jpg"]').is_displayed()
    driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH,'//div[@class="owl-item active center"]//img[@src="assets/images/slider/04.jpg"]').is_displayed()

    time.sleep(1)



    effectivity_header = driver.find_element(By.XPATH, '(//header//li)[2]//*[@aria-current="page"]')
    assert effectivity_header.is_displayed(), 'Элемента нет на экране'
    assert effectivity_header.is_enabled(), 'Элемент не кликабелен'
    assert effectivity_header.text == 'ЭФФЕКТИВНОСТЬ', f'Неверный текст. Получено {effectivity_header.text}'
    effectivity_header.click()

    time.sleep(1)



    complectation_header = driver.find_element(By.XPATH, '(//header//ul//*[@aria-current="page"])[3]')
    assert complectation_header.is_displayed(), 'Элемента нет на экране'
    assert complectation_header.is_enabled(), 'Элемент не кликабелен'
    assert complectation_header.text == 'КОМПЛЕКТАЦИЯ', f'Неверный текст. Получено {complectation_header.text}'
    complectation_header.click()
    time.sleep(2)
    driver.find_element(By.XPATH, '(//*[@id="accordionExample"]//h2)[1]//*[@aria-expanded="false"]').click()
    time.sleep(1)
    driver.execute_script('window.scrollBy(0, 1000)')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="headingTwo"]//button[@aria-expanded="false"]').click()
    time.sleep(1)
    driver.execute_script('window.scrollBy(0, 1000)')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="accordionExample"]//button[@aria-controls="collapseThree"]').click()
    time.sleep(1)
    driver.execute_script('window.scrollBy(0, 200)')
    time.sleep(2)


    comfort_header = driver.find_element(By.XPATH, '(//nav//ul//*[@aria-current="page" and @href="#comforts"])[1]')
    assert comfort_header.is_displayed(), 'Элемента нет на экране'
    assert comfort_header.is_enabled(), 'Элемент не кликабелен'
    assert comfort_header.text == 'КОМФОРТ', f'Неверный текст. Получено {comfort_header.text}'
    comfort_header.click()
    time.sleep(3)


    buy_header = driver.find_element(By.XPATH, '(//header//ul//*[@aria-current="page" and @href="#feedbacks"])[1]')
    assert buy_header.is_displayed(), 'Элемента нет на экране'
    assert buy_header.is_enabled(), 'Элемент не кликабелен'
    assert buy_header.text == 'КУПИТЬ В ЛИЗИНГ', f'Неверный текст. Получено {buy_header.text}'
    buy_header.click()

    time.sleep(2)

    driver.execute_script('window.scrollBy(0, 500)')
    driver.implicitly_wait(10)


    app_button = driver.find_element(By.XPATH, '//button[@class="feedback-btn"]')
    app_button.click()


    driver.find_element(By.XPATH, '//input[@name="Имя"]').send_keys('Michael')
    driver.find_element(By.XPATH, '//input[@name="Фамилия"]').send_keys('HOdjekn')
    driver.find_element(By.XPATH, '//input[@name="Телефон*"]').send_keys('+8393045384')
    driver.find_element(By.XPATH, '//input[@name="E-mail"]').send_keys('djfoiwefh@gmail.com')
    driver.find_element(By.XPATH, '//label[@for="checkbok"]').click()
    driver.find_element(By.XPATH, '//button[@type="submit" and @name="feed_back"]').click()


    time.sleep(2)

    driver.quit()
    driver.close()
