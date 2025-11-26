import allure
import pytest
import requests
import json



@allure.epic('Апи тесты')
@allure.feature('Обработка заявки')
@allure.story('Негативные тесты')

@allure.title('Проверка статус кода')
@pytest.mark.parametrize("url, expected_status_code", [
    ("https://superjet.rostsayt.ru/advantange", 400),
    ("https://superjet.rostsayt.ru/legacy", 400),
    ("https://superjet.rostsayt.ru/camfort", 401),
    ("https://superjet.rostsayt.ru/class", 400),
    ("https://superjet.rostsayt.ru/leasing", 400),
    ("https://superjet.rostsayt.ru/greed", 400),
])

def test_false_endpoints(url,expected_status_code):
    with allure.step('Подготовка тестовых данных'):
        url = 'https://superjet.rostsayt.ru/advantange'

        headers = {
           'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
           'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
           'priority: u=0, i'
           'sec-ch-ua: \"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"'
           'sec-ch-ua-mobile: ?0'
           'sec-ch-ua-platform: \"Windows\"'
           'sec-fetch-dest: document'
           'sec-fetch-mode: navigate'
           'sec-fetch-site: none'
           'sec-fetch-user: ?1'
           'upgrade-insecure-requests: 1'
           'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'"
        }
        payload={}


    with allure.step(f'Вызов метода {url}'):
        response = requests.request("GET", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода заявки'):
        assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}, а равен {response.status_code}'


