import time
import re

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/droppable")
    driver.execute_script("""window.scrollBy(0, 500)""")

    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    draggable = wait.until(EC.element_to_be_clickable((By.ID, "draggable")))
    droppable = wait.until(EC.element_to_be_clickable((By.ID, "droppable")))
    actions.drag_and_drop(draggable, droppable).perform()


    time.sleep(2)

    driver.quit()
