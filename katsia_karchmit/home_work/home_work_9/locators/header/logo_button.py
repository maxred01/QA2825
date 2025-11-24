import os
from katsia_karchmit.home_work.home_work_9.page.base_page import WebPage
from katsia_karchmit.home_work.home_work_9.page.elements import WebElement

class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://zrobim.by/'
        super().__init__(web_driver, url)

    logo_button = WebElement(xpath="//*[@alt='logo' and contains(concat(' ', normalize-space(@class), ' '), ' header__header-logo ')][1]")