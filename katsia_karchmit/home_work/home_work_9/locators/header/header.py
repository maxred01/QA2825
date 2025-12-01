import os
from katsia_karchmit.home_work.home_work_9.page.base_page import WebPage
from katsia_karchmit.home_work.home_work_9.page.elements import WebElement

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://zrobim.by/'
        super().__init__(web_driver, url)

    btn_header_logo = WebElement(xpath="//*[@alt='logo' and contains(concat(' ', normalize-space(@class), ' '), ' header__header-logo ')][1]")
    btn_header_menu = WebElement(xpath="//div[@class='menu-open__text']")
    btn_header_consultant = WebElement(xpath="//*[contains(concat(' ', normalize-space(@class), ' '), ' header__header ')]//button")
    name_input = WebElement(xpath='(//*[@id="feedback-name" and @name="name" and @type="text"])[2]')
    city_input = WebElement(xpath='(//*[@name="city"])[2]')
    phone_input = WebElement(xpath='(//*[@name="phone"])[2]')
    email_input = WebElement(xpath='(//*[@name="email"])[2]')
    message_textarea = WebElement(xpath='(//*[@name="comment"])[2]')
    btn_close_consultant = WebElement(xpath='//*[@fill="none"][1]')
