import uuid
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    return options


@pytest.fixture
def web_browser(request, chrome_options):
    # Используем переданные опции
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()

    # Вернуть экземпляр браузера в тестовый пример:
    yield browser

    # Безопасная проверка статуса теста
    failed = False
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        failed = True
    elif hasattr(request.node, "rep_setup") and request.node.rep_setup.failed:
        failed = True

    if failed:
        try:
            # Делаем фон белым для лучшего скриншота
            browser.execute_script("document.body.style.background = 'white';")

            # Создаем скриншот
            screenshot_path = f'screenshots/{str(uuid.uuid4())}.png'
            browser.save_screenshot(screenshot_path)

            # Прикрепляем скриншот к Allure
            allure.attach(
                browser.get_screenshot_as_png(),
                name=f"{request.function.__name__}_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Логируем URL и логи браузера
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

            # Также прикрепляем логи к Allure
            logs = "\n".join([str(log) for log in browser.get_log('browser')])
            allure.attach(
                logs,
                name=f"{request.function.__name__}_browser_logs",
                attachment_type=allure.attachment_type.TEXT
            )

        except Exception as e:
            print(f"Ошибка при создании отчетности: {e}")

    # Всегда закрываем браузер
    browser.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    # Эта функция помогает определить, что какой-то тест не прошел
    # и передать эту информацию в отчет:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption("--browser")


def get_test_case_docstring(item):
    """ Эта функция получает строку документа из тестового примера и форматирует ее
        отображая эту строку в документации вместо имени тестового примера в отчетах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Удалить лишние пробелы из строки документа:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Сгенерировать список параметров для параметризованных тестовых случаев:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Создать список на основе Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Добавить dict со всеми параметрами к названию тестового примера:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ Эта функция изменяет имена тестовых случаев «на лету».
        во время выполнения тест-кейсов.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция изменяет имена тестовых случаев «на лету»
        когда мы используем параметр --collect-only для pytest
        (чтобы получить полный список всех существующих тестовых случаев).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # Если в тестовом примере есть строка документа, нам нужно изменить ее имя на
            # эту строку документа для отображения удобочитаемых отчетов и для
            # автоматически импортировать тестовые случаи в систему управления тестированием.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
