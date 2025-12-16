import os

from katsia_karchmit.home_work.home_work_9.page.base_page import WebPage
from katsia_karchmit.home_work.home_work_9.page.elements import WebElement
from katsia_karchmit.home_work.home_work_9.page.elements import ManyWebElements


class AboutPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('ABOUT_PAGE') or 'https://zrobim.by/team.html'

        super().__init__(web_driver, url)

    text_architectural_bureau = WebElement(xpath=("//div[text()='Архитектурное бюро']"))
    text_zrobim = WebElement(xpath=('(//*[@data-scroll="title"])[1]//strong'))
    text_architecture_idea = WebElement(xpath=("(//*[contains(concat(' ', normalize-space(@class), ' '), ' philosophy ')]//h4)[1]"))
    text_project_just_beginning = WebElement(xpath=("//h4[text()='Проект — это только начало']"))
    text_team = WebElement(xpath=("//*[@id='section']//strong"))
    text_alexey_korablyov = WebElement(xpath=("(//*[@id='section']//*[contains(concat(' ', normalize-space(@class), ' '), ' worker__item-title ')])[1]"))
    text_looking_superprofessional = WebElement(xpath=("(//*[contains(concat(' ', normalize-space(@class), ' '), ' section__content ')])[7]/*[2]"))

