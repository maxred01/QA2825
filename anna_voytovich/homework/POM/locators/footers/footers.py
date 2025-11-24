import os
from DP.anna_voytovich.class_work.POM.page.base_page import WebPage
from DP.anna_voytovich.class_work.POM.page.elements import WebElement
from DP.anna_voytovich.class_work.POM.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://superjet.rostsayt.ru/#'

        super().__init__(web_driver, url)

    btn_footer_advantages = WebElement(xpath='(//footer//a[@href="#advantagers"])[1]')
    btn_footer_effectivity = WebElement(xpath='(//footer//a[@href="#effective"])[1]')
    btn_footer_complectation = WebElement(xpath='(//footer//a[@href="#comlpects"])[1]')
    btn_footer_comfort = WebElement(xpath='(//footer//a[@href="#comforts"])[1]')
    btn_footer_the_same_site = WebElement(xpath='(//*[@href="https://rostsayt.ru" and @target="_blank"])[1]')
    btn_footer_number = WebElement(xpath='(//footer//a[@href="tel:88000055187"])[1]')
    btn_footer_youtube = WebElement(xpath='(//footer//img[@alt=""])[2]')
    btn_footer_vk = WebElement(xpath='(//footer//*[@alt=""])[3]')
