import os
from anna_voytovich.class_work.class_work_12.page.base_page import WebPage
from anna_voytovich.class_work.class_work_12.page.elements import WebElement
from anna_voytovich.class_work.class_work_12.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'http://www.scania-minsk.by/'

        super().__init__(web_driver, url)

    btn_header_service_services = WebElement(xpath='(//a[@href="/service"])[1]')
