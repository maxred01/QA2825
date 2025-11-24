import time
from selenium.webdriver.common.keys import Keys
from katsia_karchmit.home_work.home_work_9.locators.menu.menu_button import MainPage




def test_completed_projects(web_browser):
    '''Этот тест проверяет раздел меню реализованные проекты'''
    driver = MainPage(web_browser)

    # 1. Открываем меню и переходим в проекты
    driver.menu_button.click()
    time.sleep(2)
    driver.completed_projects.click()
    driver.wait_page_loaded()

    # 2. Скроллим и открываем проект
    driver._web_driver.execute_script('window.scrollBy(0,1500)')
    time.sleep(3)
    driver.project_LEV_APARTMENT.click()
    driver.wait_page_loaded()

    # 3. Скроллим на странице проекта
    driver._web_driver.execute_script('window.scrollBy(0,3000)')
    time.sleep(3)

    # 4. Проверка видео
    if driver.video_element.is_presented() and driver.video_element.is_visible():
        # Кликаем на видео
        driver.video_element.click()
        time.sleep(10)

        # Пытаемся управлять видео плеером
        if driver.video_play_button.is_presented():
            driver.video_play_button.click()
            time.sleep(5)

        # Закрываем видео
        if driver.video_close_button.is_presented():
            driver.video_close_button.click()
        else:
            # Альтернативный способ закрытия через ESC
            driver._web_driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

        time.sleep(8)

    # 5. Возвращаемся в меню
    driver.menu_button.click()
    time.sleep(8)

    # Проверяем что меню открылось (виден какой-то пункт меню)
    assert driver.completed_projects.is_visible() , 'Меню не открылось после возврата'
