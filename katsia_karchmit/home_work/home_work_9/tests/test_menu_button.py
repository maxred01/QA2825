from katsia_karchmit.home_work.home_work_9.locators.menu.menu_button import MainPage

def test_menu_button(web_browser):
    '''Этот тест проверяет кнопку меню'''
    driver = MainPage(web_browser)
    assert driver.menu_button.is_visible(), 'Кнопка меню не видна на экране'
    assert driver.menu_button.is_clickable(), 'Кнопка меню некликабельна'