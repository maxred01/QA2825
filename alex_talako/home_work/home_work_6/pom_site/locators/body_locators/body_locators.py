import os

from alex_talako.home_work.home_work_6.pom_site.page.base_page import WebPage
from alex_talako.home_work.home_work_6.pom_site.page.elements import WebElement
from alex_talako.home_work.home_work_6.pom_site.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://tryhackme.com/'


        super().__init__(web_driver, url)

    btn_cookie = WebElement(xpath = '//button[text()="Got it!"]')
    btn_email = WebElement(xpath = '//*[@aria-label="Email address"]')
    btn_join_near_email = WebElement(xpath = '//*[@data-testid="sc-banner"]//button')
    btn_container_cyber_security = WebElement(xpath = '//*[@data-testid="path-card-container-0"]')
    btn_soc_level_one = WebElement(xpath = '//*[@data-testid="path-card-container-1"]')
    btn_pre_security = WebElement(xpath = '//*[@data-testid="path-card-container-2"]')
    btn_jr_penetration_tester = WebElement(xpath = '//*[@data-testid="path-card-container-3"]')
    btn_red_teaming = WebElement(xpath = '//*[@data-testid="path-card-container-4"]')
    btn_soc_level_two = WebElement(xpath = '//*[@data-testid="path-card-container-5"]')
    btn_security_engineer = WebElement(xpath = '//*[@data-testid="path-card-container-6"]')
    btn_dev_sec_ops = WebElement(xpath = '//*[@data-testid="path-card-container-7"]')
    btn_advanced_endpoint = WebElement(xpath = '//*[@data-testid="path-card-container-8"]')
    btn_defending_azure = WebElement(xpath = '//*[@data-testid="path-card-container-9"]')
    btn_att_def_aws = WebElement(xpath = '//*[@data-testid="path-card-container-10"]')
    btn_offensive_pentest = WebElement(xpath = '//*[@data-testid="path-card-container-11"]')
    btn_web_fundamentals = WebElement(xpath = '//*[@data-testid="path-card-container-12"]')
    btn_web_application = WebElement(xpath = '//*[@data-testid="path-card-container-13"]')
    btn_comp_tia = WebElement(xpath = '//*[@data-testid="path-card-container-14"]')
    btn_dot_first = WebElement(xpath = '//*[@data-testid="dot-0" and @color="default"]')
    btn_dot_second = WebElement(xpath = '//*[@data-testid="dot-1" and @color="default"]')
    btn_dot_third = WebElement(xpath = '//*[@data-testid="dot-2" and @color="default"]')
    btn_dot_fourth = WebElement(xpath = '//*[@data-testid="dot-3" and @color="default"]')
    btn_dot_fifth = WebElement(xpath = '//*[@data-testid="dot-4" and @color="default"]')
    btn_exercises_in_lesson = WebElement(xpath = '//*[@aria-label="View media Exercises in every lesson"]')
    btn_beginner_friendly = WebElement(xpath = '//span[@aria-label="View media Beginner-friendly"]')
    btn_start_hacking_instantly = WebElement(xpath = '//*[@aria-label="View media Start hacking instantly"]')
    btn_real_world_networks = WebElement(xpath = '//*[@aria-label="View media Real-world networks"]')
    btn_dot_bottom_first = WebElement(xpath = '//*[@data-testid="dot-0" and @color="secondary"]')
    btn_dot_bottom_second = WebElement(xpath = '//*[@data-testid="dot-1" and @color="secondary"]')
    btn_dot_bottom_third = WebElement(xpath = '//*[@data-testid="dot-2" and @color="secondary"]')
    btn_cyber_train_for_team = WebElement(xpath = '(//*[@role="button"])[2]')
    btn_cyber_tarin_for_students = WebElement(xpath = '(//*[@role="button"])[3]')
    btn_bottom_join_for_free = WebElement(xpath='//*[@type="button" and @data-sentry-element="StyledButton"]')
