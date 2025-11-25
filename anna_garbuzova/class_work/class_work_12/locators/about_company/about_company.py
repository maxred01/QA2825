import os

from anna_garbuzova.class_work.class_work_12.page.base_page import WebPage
from anna_garbuzova.class_work.class_work_12.page.elements import WebElement
from anna_garbuzova.class_work.class_work_12.page.elements import ManyWebElements

class AboutPage(WebPage):
    def __init__(self, web_driver, url = ''):
        if not url:
            url = os.getenv('ABOUT_PAGE') or 'http://www.scania-minsk.by/about'


        super().__init__(web_driver, url)

    text_main_about = WebElement(id='i54rqswgn_0')
    