import os

from alex_talako.class_work.class_work_10.page.base_page import WebPage
from alex_talako.class_work.class_work_10.page.elements import WebElement
from alex_talako.class_work.class_work_10.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'http://www.scania-minsk.by/'


        super().__init__(web_driver, url)

    btn_header_services = WebElement(xpath='//a[@id="iy3qsvuwp_0"]')
