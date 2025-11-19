from max_tsybulka.class_work.class_work_12.locators.service_services.service_services import MainPage


def test_header(web_browser):
    """Этот тест проверяет элементы на странице хедара"""

    driver = MainPage(web_browser)

    assert driver.btn_header_service_services.is_visible(), 'Элемент не виден на экарне'
    assert driver.btn_header_service_services.is_clickable(), 'Элемент не виден на экарне'
    assert driver.btn_header_service_services.is_presented(), 'Элемент не виден на экарне'
