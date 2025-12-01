import allure
import pytest
import requests
import json


@allure.epic('Апи тесты')
@allure.feature('Обработка заявки')
@allure.story('Позитивные тесты')


@allure.title('Проверка статус кода сайта')
@pytest.mark.parametrize("url, expected_status_code", [
    ("https://superjet.rostsayt.ru/", 200),
    ("https://superjet.rostsayt.ru/", 100),
    ("https://superjet.rostsayt.ru/", 400),
    ("https://superjet.rostsayt.ru/", 503),
    ("https://superjet.rostsayt.ru/", 104),

])

def test_status_code(url, expected_status_code):
    with allure.step('Подготовка тестовых данных '):
        url = "https://superjet.rostsayt.ru/"

        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
        }
    with allure.step(f'Вызов метода {url} '):
        response = requests.request("GET", url, headers=headers, data=payload)
    with allure.step('Проверка статус кода '):
        assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}, а равен {response.status_code}'




