import os

from alex_talako.home_work.home_work_6.pom_site.page.base_page import WebPage
from alex_talako.home_work.home_work_6.pom_site.page.elements import WebElement
from alex_talako.home_work.home_work_6.pom_site.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://tryhackme.com/'


        super().__init__(web_driver, url)

    btn_header_hacktivities = WebElement(xpath='//*[@aria-label="Navigate to Learn page"]')