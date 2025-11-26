import time
import allure

from katsia_karchmit.home_work.home_work_9.locators.menu.menu_button import MainPage

@allure.title(f'UI тест на сайте zrobim.by')
@allure.story(f'Проверка раздела меню вакансии')


def test_vacancies_button(web_browser):

    driver = MainPage(web_browser)

    # 1. Открываем меню и переходим в вакансии
    driver.menu_button.click()
    time.sleep(2)
    driver.vacancies_button.click()
    driver.wait_page_loaded()
    # 2. Заполняем анкету соискателя
    driver.text_field_name.send_keys('Karl')
    driver.text_field_surname.send_keys('Franz')
    driver.next_button.click()
    time.sleep(5)
    driver.text_field_job.send_keys('Engineer')
    driver.text_field_link_portfolio .send_keys('https://bntu.by/index.php/news/3036-ya-inzhener')
    driver.further_button.click()
    time.sleep(5)
    driver.text_field_phone.send_keys('+375291585525')
    driver.text_field_email.send_keys('test_test@gmail.com')
    # 2. Возвращаемся в меню
    driver.menu_button.click()
    time.sleep(8)

    # 3. Проверяем что меню открылось (виден какой-то пункт меню)
    assert driver.vacancies_button.is_visible(), 'Меню не открылось после возврата'


