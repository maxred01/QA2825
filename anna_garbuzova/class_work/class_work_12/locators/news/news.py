import os

from anna_garbuzova.class_work.class_work_12.page.base_page import WebPage
from anna_garbuzova.class_work.class_work_12.page.elements import WebElement
from anna_garbuzova.class_work.class_work_12.page.elements import ManyWebElements


class NewsPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('NEWS_PAGE') or 'http://www.scania-minsk.by/novosti'

        super().__init__(web_driver, url)

    text_main_news = WebElement(id='i54rqswgn_0')
