import pytest
import requests
import json
import allure

BASE_URL = "https://tryhackme.com/"
@allure.epic('Апи тесты')
@allure.feature('Проверка корректности url адреса для endpoints')
@allure.story('Проверка, что сервер отвечает 200 OK на несуществующие URL (SPA-маршрутизация)')

@pytest.mark.parametrize('status_code_expected,endpoint_to_test', [
        (200, "https://tryhackme.com/api/dest"),
        (200, "https://tryhackme.com/not-found"),
        (200, "https://tryhackme.com/asdasdgagqewr"),
        (200, "https://tryhackme.com/hacktivities"),
        (200, "https://tryhackme.com/trum-purum"),
        (200, "https://tryhackme.com/rooms"),
        (200, "https://tryhackme.com/security"),
        ])

def test_api_not_found(status_code_expected, endpoint_to_test):
    with allure.step(f'Подготовка тестовых данных для {endpoint_to_test}'):
        payload = {}
        headers = {
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',

        }

        with allure.step(f'Вызов метода: {endpoint_to_test}'):
            response = requests.request("GET", endpoint_to_test, headers=headers, data=payload, allow_redirects=True)
        with allure.step(f'Проверка статус кода конечной страницы'):
            assert response.status_code == status_code_expected, \
                f'Статус код не равен {status_code_expected}. Получен {response.status_code} для URL {response.url}'


