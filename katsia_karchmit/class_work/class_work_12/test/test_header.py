from katsia_karchmit.class_work.class_work_12.locators.service_services.service_services import MainPage

def test_header(web_browser):
    '''Этот тест проверяет элемент на странице хедер'''

    driver = MainPage(web_browser)

    assert driver.btn_header_service_services.is_visible(), 'Элемент не виден на экране'