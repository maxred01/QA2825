from katsia_karchmit.home_work.home_work_9.locators.header.logo_button import MainPage

def test_logo_button(web_browser):
    '''Этот тест проверяет кнопку логотипа'''
    driver = MainPage(web_browser)
    assert driver.logo_button.is_visible(), 'Кнопка логотипа не видна на экране'
    assert driver.logo_button.is_clickable(), 'Кнопка логотипа некликабельна'