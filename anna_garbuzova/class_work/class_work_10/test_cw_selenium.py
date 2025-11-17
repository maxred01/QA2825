import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://superjet.rostsayt.ru/#advantagers')
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/01.jpg"]').is_displayed()
    driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/02.jpg"]').is_displayed()
    driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/03.jpg"]').is_displayed()
    driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/04.jpg"]').is_displayed()

    driver.quit()
    driver.close()