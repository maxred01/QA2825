from max_tsybulka.class_work.class_work_12.locators.about_compane.about_compane import AboutPage
import pytest_check as check


def test_text(web_browser):
    """Этот тест проверяет правильность текста"""

    driver = AboutPage(web_browser)


    check.equal(driver.text_main_about.get_text(), 'О ком676767пании', 'Неверный текст')
