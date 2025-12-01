import os
from katsia_karchmit.home_work.home_work_9.page.base_page import WebPage
from katsia_karchmit.home_work.home_work_9.page.elements import WebElement

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://zrobim.by/'
        super().__init__(web_driver, url)

    menu_button = WebElement(xpath='//div[@class="menu-open__text"]')
    # Реализованные проекты
    completed_projects = WebElement(xpath='//*[text()="Реализованные проекты"]')
    project_LEV_APARTMENT = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' category__item-title ') and text()='LEV APARTMENT'])[1]")
    video_element = WebElement(xpath="//*[@data-caption='LEV APARTMENT' and contains(@class, 'youtube__item')]")
    video_play_button = WebElement(xpath="//button[@class='ytp-play-button ytp-button']")
    video_close_button = WebElement(xpath="//*[contains(@class, 'fancybox-slide')]")

    # Контакты
    contacts_button = WebElement(xpath='//a[text()="Контакты"]')
    text_field_name_contacts = WebElement(xpath='(//*[@name="name"])[1]')
    text_field_city = WebElement(xpath='(//*[@name="city"])[1]')
    text_field_phone_contacts = WebElement(xpath='(//*[@name="phone"])[1]')
    text_field_email_contacts = WebElement(xpath='(//*[@id="feedback-email"])[1]')
    text_field_interest_contacts = WebElement(xpath='//*[@id="feedback-comment"]')





