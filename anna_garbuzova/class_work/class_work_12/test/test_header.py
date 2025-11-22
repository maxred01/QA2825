from anna_garbuzova.class_work.class_work_12.locators.services.servises import MainPage


def test_header(web_browser):
    '''Этот тест проверяет элементы на странице хедера'''

    driver = MainPage(web_browser)

    assert driver.btn_header_services.is_visible(), 'Элемент не виден на экране'