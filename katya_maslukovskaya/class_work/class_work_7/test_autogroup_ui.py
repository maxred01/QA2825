import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#поиск элементов главной менюшки главной страницы
def test_menu_autogroup():
    driver = webdriver.Chrome()
    driver.get('https://autogroup.by/')
    time.sleep(2)
    data=[
        (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[1]"), 'Кнопки Направления нет'),
        (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[2]"),'Кнопки Каталог нет'),
        (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[3]"),'Кнопки Доставка нет'),
        (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[4]"),'Кнопки Инфо нет'),
        (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[5]"),'Кнопки Услуги нет'),
        (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[6]"),'Кнопки Оплата нет'),
        (driver.find_element(By.XPATH,"(//header//a)[32]"),'Кнопки Доставка нет')
    ]

    for element, text in data:
        assert element.is_enabled(), f'Элемент {text} не кликабелен'
        assert element.is_displayed(), f'Элемента {text} нет'

    element_one = driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[1]")
    assert element_one.is_displayed, 'Элемента нет'
    assert element_one.is_enabled, 'Элемент не кликабелен'

    element_two = driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[2]")
    assert element_two.is_displayed, 'Элемента нет'
    assert element_two.is_enabled, 'Элемент не кликабелен'

    element_three = driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[3]")
    assert element_three.is_displayed, 'Элемента нет'
    assert element_three.is_enabled, 'Элемент не кликабелен'

    element_four = driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[4]")
    assert element_four.is_displayed, 'Элемента нет'
    assert element_four.is_enabled, 'Элемент не кликабелен'

    element_five = driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[5]")
    assert element_five.is_displayed, 'Элемента нет'
    assert element_five.is_enabled, 'Элемент не кликабелен'

    element_six = driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[6]")
    assert element_six.is_displayed, 'Элемента нет'
    assert element_six.is_enabled, 'Элемент не кликабелен'

    element_seven = driver.find_element(By.XPATH,"(//header//a)[32]")
    assert element_seven.is_displayed, 'Элемента нет'
    assert element_seven.is_enabled, 'Элемент не кликабелен'