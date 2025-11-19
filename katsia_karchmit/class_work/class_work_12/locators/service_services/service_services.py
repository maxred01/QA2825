import os

from katsia_karchmit.class_work.class_work_12.page.base_page import WebPage
from katsia_karchmit.class_work.class_work_12.page.elements import WebElement
#from katsia_karchmit.class_work.class_work_12.page.base_page import ManyWebElement

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'http://www.scania-minsk.by/'

        super().__init__(web_driver, url)
    btn_header_service_services = WebElement(xpath='(//a[@href="/service"])[1]')
