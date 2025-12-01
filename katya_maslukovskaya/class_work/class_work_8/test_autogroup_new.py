# # #if clicable
# # #driver.back
# # #href ссылка
# #
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# #
# # URL_CONST='https://autogroup.by/'
# #
# # def test_menu_autogroup():
# #     driver = webdriver.Chrome()
# #     driver.get('https://autogroup.by/')
# #     time.sleep(5)
# #     data=[
# #         (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' filter-country__btn ')])[2]"), 'Европа', 'main_page-eu/'),
# #         (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' filter-country__btn ')])[3]"), 'Корея', 'main_page-korea/'),
# #         (driver.find_element(By.XPATH,"(//*[contains(concat(' ', normalize-space(@class), ' '), ' filter-country__btn ')])[4]"), 'Китай', 'main_page-kitay/')
# #
# #     ]
# #
# #     for element, text, url in data:
# #         driver.find_element((By.XPATH,"(//header//a)[8]")).click()
# #         time.sleep(5)
# #         element.click()
# #         assert driver.current_url==URL_CONST+url, f'Неверная ссылка{text}'
# #
# #     driver.quit()
# #     driver.close()
# #
# #
# # def test_image_autogroup():
# #     driver=webdriver.Chrome
# #     driver.get('https://autogroup.by/')
# #     time.sleep(7)
# #
# #     assert driver.find_element(By.XPATH,'//*[@alt="KIA K5"]').click()
#
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
#
#
# def test_selenium():
#
#     driver = webdriver.Chrome()
#     driver.get('https://superjet.rostsayt.ru/#advantagers')
#     time.sleep(5)
#     assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/01.jpg"]').is_displayed()
#     driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
#     time.sleep(2)
#
#     assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/02.jpg"]').is_displayed()
#     driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
#     time.sleep(2)
#
#     assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/03.jpg"]').is_displayed()
#     driver.find_element(By.XPATH, '//button[@class="owl-next"]').click()
#     time.sleep(2)
#
#     assert driver.find_element(By.XPATH, '//div[@class="owl-item active center"]//img[@src="assets/images/slider/04.jpg"]').is_displayed()
#
#     driver.quit()
#     driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_menu_autogroup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://autogroup.by/catalog-usa/')
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@name="MIN"]').click()
    driver.find_element(By.XPATH, '//*[@name="MIN"]').send_keys('20000')

    driver.find_element(By.XPATH, '//*[@name="MAX"]').click()
    driver.find_element(By.XPATH, '//*[@name="MAX"]').send_keys('70000')

    #driver.execute_script("""window.scrollBy(0,350""")
    count_len=driver.find_elements(By.XPATH, "//div[@class='main_page-item *]")
    print(len(count_len))

    driver.find_element(By.XPATH, '//div[@id="view-Mark"]').click()
    driver.find_element(By.XPATH,'div[id')

    assert len(count_len)>=3
    assert len(count_len)==3
    assert len(count_len)==total
    assert len(count_len) is not None


    driver.quit()
    driver.close()
#массив фиат и сколько выдало фиатов