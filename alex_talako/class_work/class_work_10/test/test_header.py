from alex_talako.class_work.class_work_10.locators.services.services import MainPage



def test_header(web_browser):
    """Этот тест проверяет элементы на странице хэдера"""

    driver = MainPage(web_browser)

    assert driver.btn_header_services.is_visible(), 'Элемент отсутствует на экране'
