import os

from alex_talako.class_work.class_work_10.page.base_page import WebPage
from alex_talako.class_work.class_work_10.page.elements import WebElement
from alex_talako.class_work.class_work_10.page.elements import ManyWebElements


class AboutPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('ABOUT_PAGE') or 'http://www.scania-minsk.by/about'


        super().__init__(web_driver, url)

    text_name_about = WebElement(id="i54rqswgn_0")
    text_side_bar_1 = WebElement(id="ix8ijs8ob_0")
    text_side_bar_2 = WebElement(id="i9jgnid7m_1")
    text_side_bar_3 = WebElement(id="i9jgnid7m_2")
    text_side_bar_4 = WebElement(id="i9jgnid7m_3")
    text_side_bar_5 = WebElement(id="i9jgnid7m_4")


