import os

from alex_talako.home_work.home_work_6.pom_site.page.base_page import WebPage
from alex_talako.home_work.home_work_6.pom_site.page.elements import WebElement
from alex_talako.home_work.home_work_6.pom_site.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://tryhackme.com/'


        super().__init__(web_driver, url)

    btn_cookie = WebElement(xpath="//button[contains(., 'Got it!')]")
    btn_header_hacktivities = WebElement(xpath='//*[@aria-label="Navigate to Learn page"]')
    btn_header_practice = WebElement(xpath='//*[@aria-label="Toggle dropdown for Practice"]')
    btn_header_compete = WebElement(xpath='//*[@aria-label="Toggle dropdown for Compete"]')
    btn_header_education = WebElement(xpath='//*[@aria-label="Toggle dropdown for Education"]')
    btn_header_business = WebElement(xpath='//*[@aria-label="Navigate to Business page"]')
    btn_header_pricing = WebElement(xpath='//*[@aria-label="Navigate to Pricing page"]')
    btn_header_search = WebElement(xpath='//*[@data-testid="search-btn"]')
    btn_header_log_in = WebElement(xpath='(//*[@data-link="outlined"])[2]')
    btn_header_join_for_free = WebElement(xpath='//*[@data-link="join"]')
