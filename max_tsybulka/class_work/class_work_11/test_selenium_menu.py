import time
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_selenium():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/menu")
    driver.execute_script("""window.scrollBy(0, 200)""")

    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    main_menu_item_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Main Item 2')]")))
    actions.move_to_element(main_menu_item_2).perform()

    sub_sub_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'SUB SUB LIST »')]")))
    actions.move_to_element(sub_sub_list).perform()

    sub_sub_item_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sub Sub Item 2')]")))
    actions.move_to_element(sub_sub_item_2).perform()

    time.sleep(2)

    driver.quit()
