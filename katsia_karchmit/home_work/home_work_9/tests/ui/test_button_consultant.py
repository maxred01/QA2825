import allure

from katsia_karchmit.home_work.home_work_9.locators.consultant.button_consultant import MainPage

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка кнопки консультант и заполнение всех полей формы')

def test_button_consultant(web_browser):


    driver = MainPage(web_browser)

    # Проверка и открытие формы
    assert driver.btn_button_consultant_consultant.is_visible(), 'Кнопка консультанта не видна'
    assert driver.btn_button_consultant_consultant.is_clickable(), 'Кнопка консультанта некликабельна'
    driver.btn_button_consultant_consultant.click()

    # Заполнение всех доступных полей формы
    driver.name_input.send_keys('Karl')
    driver.city_input.send_keys('Минск')
    driver.phone_input.send_keys('+375291234567')
    driver.email_input.send_keys('tests@example.com')
    driver.message_textarea.send_keys('Нужна консультация по ремонту')

    # Закрытие формы
    assert driver.close_button.is_clickable(), 'Кнопка закрытия некликабельна'
    driver.close_button.click()