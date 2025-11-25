from anna_garbuzova.class_work.class_work_12.locators.news.news import NewsPage
import pytest_check as check

def test_text(web_browser):
    # '''Этот тест проверяет текст на странице Новости'''

    driver = NewsPage(web_browser)

    check.equal(driver.text_main_news.get_text(), 'Новости','Неверный текст')