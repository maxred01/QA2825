import os
from anna_voytovich.homework.POM.page.base_page import WebPage
from anna_voytovich.homework.POM.page.elements import WebElement
from anna_voytovich.homework.POM.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://superjet.rostsayt.ru/#'

        super().__init__(web_driver, url)

    btn_arrow_next = WebElement(xpath='//button[@class = "owl-next"]')
    btn_arrow_previous = WebElement(xpath='//button[@class = "owl-prev"]')
    btn_dropdown_tech_characteristics = WebElement(xpath='//button[@data-bs-target = "#collapseOne"]')
    btn_dropdown_weigh_characteristics = WebElement(xpath='//button[@data-bs-target = "#collapseTwo"]')
    btn_dropdown_size = WebElement(xpath='//button[@data-bs-target = "#collapseThree"]')
    btn_leave_an_app = WebElement(xpath='//button[@class = "feedback-btn"]')
