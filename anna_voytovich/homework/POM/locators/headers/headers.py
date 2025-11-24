import os
from DP.anna_voytovich.class_work.POM.page.base_page import WebPage
from DP.anna_voytovich.class_work.POM.page.elements import WebElement
from DP.anna_voytovich.class_work.POM.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://superjet.rostsayt.ru/#'

        super().__init__(web_driver, url)

    btn_header_advantages = WebElement(xpath='(//*[@aria-current="page" and @href="#advantagers"])[1]')
    btn_header_effectivity = WebElement(xpath='(//header//li)[2]//*[@aria-current="page"]')
    btn_header_complectation = WebElement(xpath='(//header//ul//*[@aria-current="page"])[3]')
    btn_header_comfort = WebElement(xpath='(//nav//ul//*[@aria-current="page" and @href="#comforts"])[1]')
    btn_header_buy = WebElement(xpath='(//header//ul//*[@aria-current="page" and @href="#feedbacks"])[1]')
