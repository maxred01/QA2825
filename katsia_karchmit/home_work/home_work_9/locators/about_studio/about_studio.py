import os

from katsia_karchmit.home_work.home_work_9.page.base_page import WebPage
from katsia_karchmit.home_work.home_work_9.page.elements import WebElement
from katsia_karchmit.home_work.home_work_9.page.elements import ManyWebElements


class AboutPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('ABOUT_PAGE') or 'https://zrobim.by/team.html'

        super().__init__(web_driver, url)

    text_architectural_bureau = WebElement(xpath=("//div[text()='Архитектурное бюро']"))
    text_zrobim = WebElement(xpath=('(//*[@data-scroll="title"])[1]//strong'))