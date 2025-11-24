import os

from alex_talako.home_work.home_work_6.pom_site.page.base_page import WebPage
from alex_talako.home_work.home_work_6.pom_site.page.elements import WebElement
from alex_talako.home_work.home_work_6.pom_site.page.elements import ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv('MAIN_PAGE') or 'https://tryhackme.com/'


        super().__init__(web_driver, url)

    btn_cookie = WebElement(xpath="//button[text()='Got it!']")
    btn_hands_on_labs = WebElement(xpath= '//*[@data-testid="top-footer"]//a[@href="/hacktivities"]')
    btn_for_business = WebElement(xpath ='//*[@data-testid="top-footer"]//a[@href="/business"]')
    btn_for_education = WebElement(xpath ='//*[@data-testid="top-footer"]//a[@href="/classrooms"]')
    btn_competitive_hacking = WebElement(xpath ='//*[@data-testid="top-footer"]//a[@href="/games/koth"]')
    btn_defensive_certifications = WebElement(xpath ='//*[@data-testid="top-footer"]//a[@href="/certification/security-analyst-level-1"]')
    btn_about_us = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="/about"]')
    btn_newsroom = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="/resources/newsroom"]')
    btn_blog = WebElement(xpath = '//*[@data-testid="top-footer"]//*[@href="/resources/blog"]')
    btn_glossary = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="/glossary"]')
    btn_work_at_tryhackme = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="https://careers.tryhackme.com"]')
    btn_careers_in_cyber = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="/careers"]')
    btn_buy_vouchers = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="/subscriptions"]')
    btn_swag_shop = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="https://store.tryhackme.com"]')
    btn_contact_us = WebElement(xpath = '//*[@aria-label="contact us" and @href="/contact"]')
    btn_forum = WebElement(xpath = '//*[@data-testid="top-footer"]//a[@href="/forum"]')
    btn_privacy_policy = WebElement(xpath = '//*[@data-testid="bottom-footer"]//a[@href="/legal/privacy-policy"]')
    btn_terms_of_use = WebElement(xpath = '//*[@data-testid="bottom-footer"]//a[@href="/legal/terms-of-use"]')
    btn_ai_terms_of_use = WebElement(xpath = '//*[@data-testid="bottom-footer"]//a[@href="/legal/ai-terms-of-use"]')
    btn_acceptable_use_policy = WebElement(xpath = '//*[@data-testid="bottom-footer"]//a[@href="/legal/acceptable-use-policy"]')
    btn_cookie_policy = WebElement(xpath = '//*[@data-testid="bottom-footer"]//a[@href="/legal/cookie-policy"]')
    btn_follow_us_on_x = WebElement(xpath = '//*[@aria-label="Follow us on X"]')
    btn_linkedin = WebElement(xpath = '//*[@aria-label="Follow us on Linkedin"]')
    btn_discord = WebElement(xpath = '//*[@aria-label="Join Discord"]')
    btn_follow_us_on_facebook = WebElement(xpath = '//*[@aria-label="Follow us on Facebook"]')
    btn_follow_us_on_youtube = WebElement(xpath = '//*[@aria-label="Follow us on our Youtube channel"]')
    btn_follow_us_on_instagram = WebElement(xpath = '//*[@aria-label="Follow us on Instagram"]')
    btn_follow_us_on_pinterest = WebElement(xpath = '//*[@aria-label="Follow us on Pinterest"]')
    btn_help_button = WebElement(xpath = '//div[@class="intercom-lightweight-app-launcher-icon intercom-lightweight-app-launcher-icon-open"]')


