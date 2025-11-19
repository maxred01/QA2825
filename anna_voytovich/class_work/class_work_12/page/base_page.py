import time
import requests

from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebPage(object):
    _web_driver = None

    def __init__(self, web_driver, url=''):
        self._web_driver = web_driver
        self.get(url)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self.__getattribute__(name)._set_value(self._web_driver, value)
        else:
            super(WebPage, self).__setattr__(name, value)

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)

        if not item.startswith('_') and not callable(attr):
            attr._web_driver = self._web_driver
            attr._page = self

        return attr

    def get(self, url):
        self._web_driver.get(url)
        self.wait_page_loaded()

    def go_back(self):
        self._web_driver.back()
        self.wait_page_loaded()

    def refresh(self):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def screenshot(self, file_name='screenshot.png'):
        self._web_driver.save_screenshot(file_name)

    def scroll_down(self, offset=0):
        """ Прокрутите страницу вниз. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """ Прокрутить страницу вверх. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe):
        """ Переключитесь на iframe по его имени. """
        self._web_driver.switch_to.frame(iframe)

    def get_cookies(self):
        """ Этот метод выводит все доступные файлы cookie для текущей сессии. """
        return self._web_driver.get_cookies()

    def add_cookie(self, name, value):
        """ Этот метод помогает настроить файл cookie для сессии. """
        return self._web_driver.add_cookie(name=name, value=value)

    def switch_to_alert_accept(self):
        """ Deprecated use switch_to_alert. """
        self._web_driver.switch_to.alert.accept()

    def switch_to_window(self, window=0):
        """ Переключитесь на вкладку по его индексу. """
        self._web_driver.switch_to.window(self._web_driver.window_handles[window])

    def switch_out_iframe(self):
        """ Отменить фокус iframe. """
        self._web_driver.switch_to.default_content()

    def validate_html(self, url):
        """Функция для проверки валидации HTML страницы"""
        validator_url = 'https://validator.w3.org/nu/?out=json'
        headers = {'Content-Type': 'text/html; charset=utf-8'}
        data = requests.get(url).text
        response = requests.post(validator_url, headers=headers, data=data.encode('utf-8'))
        results = response.json()
        return results

    def get_current_url(self):
        """ Возвращает URL текущего браузера. """
        return self._web_driver.current_url

    def execute_script(self, script):
        """ Возвращает JS скрипт. """
        return self._web_driver.execute_script(script)

    def get_page_source(self):
        """ Возвращает тело текущей страницы. """

        source = ''
        try:
            source = self._web_driver.page_source
        except:
            print(colored('Can not get page source', 'red'))

        return source

    def check_js_errors(self, ignore_list=None):
        """ Эта функция проверяет ошибки JS на странице. """

        ignore_list = ignore_list or []

        logs = self._web_driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):
        """ Эта функция ждет, пока страница не будет полностью загружена.
            Мы используем много разных способов определить, загружена страница или нет.:
            1) Проверить статус JS
            2) Проверить модификацию в исходном коде страницы
            3) Убедитесь, что все изображения загружены полностью
               (Примечание: по умолчанию эта проверка отключена)
            4) Убедиться, что ожидаемые элементы, представленные на странице
        """

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Получить исходный код страницы для отслеживания изменений в HTML:
        source = ''
        try:
            source = self._web_driver.page_source
        except:
            pass

        # Подождать, пока страница загрузится (и прокрутить ее, чтобы убедиться, что все объекты будут загружены):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Прокрутить вниз и подождите, пока страница загрузится:
                try:
                    self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Проверьть не изменился ли источник страницы
                new_source = ''
                try:
                    new_source = self._web_driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Подождить когда какой-то элемент исчезнет:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self._web_driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Игнорировать ошибки тайм-аута

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self._web_driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Игнорировать ошибки тайм-аута

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Проверить два раза, что страница полностью загружена:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Поднимать вверх (скролл):
        self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')