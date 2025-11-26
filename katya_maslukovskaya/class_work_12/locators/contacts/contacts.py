import os
from xml.etree.ElementPath import xpath_tokenizer

from katya_maslukovskaya.class_work_12.page.base_page import WebPage
from katya_maslukovskaya.class_work_12.page.elements import WebElement
from katya_maslukovskaya.class_work_12.page.elements import ManyWebElements

class Contacts(WebPage):
    def __init__(self,web_driver,url=''):
        if not url:
            url=os.getenv('CONTACTS') or 'https://autogroup.by/contacts/'

        super().__init__(web_driver,url)

    btn_button_minsk=WebElement(xpath='(//*[@role="button"])[3]')
    btn_button_gomel=WebElement(xpath='(//*[@role="button"])[4]')
    btn_button_grodno=WebElement(xpath='(//*[@role="button"])[5]')
    btn_button_brest=WebElement(xpath='(//*[@role="button"])[6]')