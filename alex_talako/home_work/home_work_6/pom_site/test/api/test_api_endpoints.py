import pytest
import requests
import json
import allure

BASE_URL = "https://tryhackme.com/"
@allure.epic('API тесты')
@allure.feature('Проверка основных публичных страниц')
@allure.title('Проверка доступности и статус кода основных Endpoints')
@pytest.mark.parametrize('endpoint, expected_status_code', [
    ("https://tryhackme.com/challenges", 200),
    ("https://tryhackme.com/dashboard", 200),
    ("https://tryhackme.com/", 200),
    ("https://tryhackme.com/login", 200),
    ("https://tryhackme.com/register", 200),
])
def test_public_endpoints_status(endpoint, expected_status_code):
    with allure.step(f'Подготовка тестовых данных для {endpoint}'):
        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        }

        response = None

    with allure.step(f'Вызов метода: {endpoint}'):
        follow_redirects = expected_status_code == 200
        response = requests.request("GET", endpoint, headers=headers, data=payload, allow_redirects=follow_redirects)

    with allure.step(f'Проверка статус кода для: {endpoint}'):
        assert response.status_code == expected_status_code, \
            f'Статус код не совпадает. Ожидался {expected_status_code}, получен {response.status_code}'