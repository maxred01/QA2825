import time
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL_CONST = "https://zrobim.by/"


def test_selenium():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://autogroup.by/catalog-usa")

    driver.find_element(By.XPATH, '//input[@id="MIN"]').send_keys("10000")
    driver.find_element(By.XPATH, '//input[@id="MAX"]').send_keys("11000")
    driver.execute_script("""window.scrollBy(0, 100)""")
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)
    driver.execute_script("""window.scrollBy(0, 350)""")
    count_len = driver.find_elements(By.XPATH, '//div[@class="catalog-item "]')
    print(len(count_len))

    driver.find_element(By.XPATH, '//div[@id="view-MARK"]').click()
    ewqw = driver.find_element(By.XPATH, '//div[@id="MARK"]').text

    number = re.findall(r"\((\d+)\)", ewqw)
    total = sum(int(num) for num in number)

    assert len(count_len) >= 3
    assert len(count_len) == 3
    assert len(count_len) is not None
    assert len(count_len) == total

    driver.quit()