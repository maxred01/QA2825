import os
from xml.etree.ElementPath import xpath_tokenizer

from katya_maslukovskaya.class_work_12.page.base_page import WebPage
from katya_maslukovskaya.class_work_12.page.elements import WebElement
from katya_maslukovskaya.class_work_12.page.elements import ManyWebElements

class MainPage(WebPage):
    def __init__(self,web_driver,url=''):
        if not url:
            url=os.getenv('MAIN_PAGE') or 'https://autogroup.by/'

        super().__init__(web_driver,url)

    btn_header_directions=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[1]")
    btn_header_catalog=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[2]")
    btn_header_delivery=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[3]")
    btn_header_info=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[4]")
    btn_header_services=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[5]")
    btn_header_payment=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' dropdown__title ')])[6]")
    btn_header_contacts=WebElement(xpath="(//header//a)[32]")
    btn_header_telegram=WebElement(xpath='(//*[@target="_blank"])[4]')
    btn_header_viber=WebElement(xpath='(//*[@target="_blank"])[5]')
    btn_header_instagram=WebElement(xpath='(//*[@target="_blank"])[6]')
    btn_header_youtube=WebElement(xpath='(//*[@target="_blank"])[7]')
    btn_header_phone_number=WebElement(xpath="//*[contains(concat(' ', normalize-space(@class), ' '), ' phone-link ')]")
    btn_body_favorites=WebElement(xpath="//div[@class='favorites-link-button']")
    btn_body_watch_calatog_auto=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' top-banner__nav-item ')])[1]")
    btn_body_consultation=WebElement(xpath='//*[@data-target="anchor"]')
    btn_body_check_price_auto=WebElement(xpath="//*[contains(concat(' ', normalize-space(@class), ' '), ' popup-link-auto-btn ')]")
    btn_body_check_auto=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' top-banner__nav-item ')])[4]")
    btn_body_link_text=WebElement(xpath="//*[contains(concat(' ', normalize-space(@class), ' '), ' iaa__text-wrap ')]//a")
    btn_body_auto_for_yourself=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' custom-tab ')])[1]")
    btn_body_corporate_auto=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' custom-tab ')])[2]")
    btn_body_clear_delivery_pay=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' section-tariffs__card-btn ')])[1]")
    btn_body_standart_pay=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' section-tariffs__card-btn ')])[2]")
    btn_body_all_included_pay=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' section-tariffs__card-btn ')])[3]")
    #btn_body_corporate_individual_pay=WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' section-tariffs__card-btn ')])[4]")
    #пропуск корпоративный корпоративный тариф
    #пропущена лента каталог авто из-за границы
    btn_body_button_left=WebElement(xpath='(//*[@aria-label="Previous slide"])[1]')
    btn_body_button_right=WebElement(xpath='(//*[@aria-label="Next slide"])[1]')
    btn_body_button_round_one=WebElement(xpath='(//span[@aria-label="Go to slide 1"])[1]')
    btn_body_button_round_two=WebElement(xpath='(//span[@aria-label="Go to slide 2"])[1]')
    btn_body_button_round_three=WebElement(xpath='(//span[@aria-label="Go to slide 3"])[1]')
    btn_body_button_round_four=WebElement(xpath='(//span[@aria-label="Go to slide 4"])[1]')
    btn_body_button_round_five=WebElement(xpath='(//span[@aria-label="Go to slide 5"])[1]')
    btn_body_button_round_six=WebElement(xpath='(//span[@aria-label="Go to slide 6"])[1]')
    btn_body_button_round_seven=WebElement(xpath='(//span[@aria-label="Go to slide 7"])[1]')
    btn_body_button_round_eight=WebElement(xpath='(//span[@aria-label="Go to slide 8"])[1]')
    btn_body_button_round_nine=WebElement(xpath='//span[@aria-label="Go to slide 9"]')
    btn_body_button_watch_all_auto=WebElement(xpath="//a[@class='btn automize-selected-node automize-selected-transition']")
    btn_body_application_name=WebElement(xpath="//input[@id='name-msf']")
    btn_body_application_phone=WebElement(xpath="//input[@id='tel-mst']")
    btn_body_application_communication_method=WebElement(xpath="//div[@class='select__current new-select']")
    btn_body_application_communication_method_phone=WebElement(xpath="//div[@class='new-select__item automize-selected-node automize-selected-transition']")
    btn_body_application_communication_method_tg=WebElement(xpath="(//div[@class='new-select__item'])[1]")
    btn_body_application_communication_method_viber=WebElement(xpath="(//div[@class='new-select__item'])[2]")
    btn_body_application_communication_method_whatsapp=WebElement(xpath="(//div[@class='new-select__item'])[3]")
    btn_body_acception_data=WebElement(xpath="//label[@for='consent-checkbox-msf']")
    btn_body_submit_app=WebElement(xpath="//input[@class='btn col-50 col-100-xs']")








#напимсать файл по всему на главной страницы как выше и ему все проверки
# асерты хедеры футеры что все визибл кликбл ис презентед

# //div[contains(text(), 'First Name')]
