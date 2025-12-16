import os
from katsia_karchmit.home_work.home_work_9.page.base_page import WebPage
from katsia_karchmit.home_work.home_work_9.page.elements import WebElement

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://zrobim.by/'
        super().__init__(web_driver, url)

    text_order_project = WebElement(xpath="(//div[contains(concat(' ', normalize-space(@class), ' '), ' footer__subtitle ') and text()='Заказать проект'])")
    text_cooperation = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' footer__subtitle ') and text()='Сотрудничество'])")
    btn_footer_language = WebElement(xpath="//*[contains(concat(' ', normalize-space(@class), ' '), ' header ')]//p[text()='Язык']")
    btn_footer_questionnaire = WebElement(xpath='(//*[@href="/vakansii.html"])[2]')
    btn_footer_offer = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' bold ')])[2]")
    text_field_name = WebElement(xpath='//input[@name="name"][1]')
    text_field_surname = WebElement(xpath='//*[@name="lastname"]')
    next_button = WebElement(xpath='((//*[@data-styles-apllied="true"])[1]//button)[1]')
    text_field_job = WebElement(xpath='(//*[@type="string"])[1]')
    text_field_link_portfolio = WebElement(xpath='(//*[@type="string"])[2]')
    further_button = WebElement(xpath='((//*[@data-styles-apllied="true"])[1]//button)[2]')
    text_field_phone = WebElement(xpath='(//input[@name="phone"])[1]')
    text_field_email = WebElement(xpath='(//*[@name="email"])[1]')
    btn_send = WebElement(xpath="(//*[@type='submit' and contains(concat(' ', normalize-space(@class), ' '), ' b24-form-btn ')])[1]")
    text_thank_you= WebElement(xpath='(//*[@data-styles-apllied="true"])[1]//p')
