import pytest
import requests
import allure


BASE_URL = "https://tryhackme.com"
SECURITY_HEADERS_TO_CHECK = [
    ('Content-Security-Policy', False),
    ('Strict-Transport-Security', False),
    ('X-Content-Type-Options', False),
    ('Content-Type', True),
    ('Server', True),
]

@allure.epic('Доступность сайта')
@allure.feature('Главная страница')
@allure.story('Проверка работы главной страницы сайта')
@pytest.mark.public
@pytest.mark.availability
def test_main_website_availability():
    """Проверяет, что главная страница сайта TryHackMe отвечает со статусом 200 OK и содержит ожидаемый HTML-контент."""

    url = f'{BASE_URL}/'

    with allure.step(f'Отправка GET запроса к {url} с таймаутом 10 секунд'):
        response = requests.get(url, timeout=10)

    with allure.step('Проверка статус-кода HTTP 200 OK'):
        assert response.status_code == 200, \
            f'Ожидался статус 200 OK, но получен {response.status_code}'

    with allure.step("Проверка наличия ключевого слова 'TryHackMe' в теле ответа"):
        assert "TryHackMe" in response.text, "Ключевое слово 'TryHackMe' не найдено в теле ответа"


@allure.epic('Тестирование безопасности')
@allure.feature('HTTP Заголовки')
@allure.story('Проверка наличия или отсутствия ключевых заголовков безопасности')
@pytest.mark.public
@pytest.mark.headers
@pytest.mark.parametrize('header_name, expected_presence', SECURITY_HEADERS_TO_CHECK)
def test_security_headers_presence(header_name, expected_presence):

    url = f'{BASE_URL}/login'

    with allure.step(f'Отправка GET запроса к {url} с таймаутом 10 секунд'):
        response = requests.get(url, timeout=10)

    with allure.step('Проверка, что сайт доступен (200 OK) перед анализом заголовков'):
        assert response.status_code == 200, 'Сайт должен быть доступен для проверки заголовков'

    headers = response.headers

    with allure.step(f'Проверка наличия заголовка "{header_name}" (Ожидание: {expected_presence})'):

        is_present = header_name in headers

        if expected_presence:
            assert is_present, f'Ошибка.Ожидали наличие заголовка "{header_name}", но он отсутствует!'
        else:
            if is_present:
                pytest.fail(f'Баг исправлен. Заголовок "{header_name}" существует')
            else:
                pytest.skip(f'Подтверждение бага. Заголовок "{header_name}" отсутствует')

    with allure.step('Проверка наличия базового заголовка Content-Type'):
        assert 'Content-Type' in headers, "Отсутствует базовый заголовок Content-Type"
        assert 'text/html' in headers['Content-Type'], "Ожидается Content-Type 'text/html'"

    with allure.step('Проверка наличия заголовка Server'):
        assert 'Server' in headers, "Отсутствует заголовок Server (Cloudflare)"

@allure.epic('Доступность сайта')
@allure.feature('Favicon')
@allure.story('Проверка наличия иконки сайта')
def test_check_favicon_exists():
    url = f'{BASE_URL}/favicon.ico'

    with allure.step(f'Отправка GET запроса к {url}'):
        response = requests.get(url)

    with allure.step('Проверка статус-кода HTTP 200 OK'):
        assert response.status_code == 200

    with allure.step('Проверка типа контента (Content-Type)'):
        assert 'image/vnd.microsoft.icon' in response.headers['Content-Type']

