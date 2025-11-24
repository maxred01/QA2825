import requests
import json
import pytest
import allure

@allure.epic('Апи тесты')
@allure.feature('Обработка заявки')
@allure.story('Позитивные тесты')

@allure.title('Проверка ввода адреса электронной почты')
@pytest.mark.parametrize("email" , [None,
                                    "tester@tests.com",
                                    " tester@tests.com",
                                    "tester @tests.com",
                                    "@tests.ru",
                                    "tester",
                                    "374098-",
                                    "vj;oajf",
                                    "",
                                    " ",
                                    "tester@tests.com ",
                                    "tester@tests.",
                                    "tester@.com",

])

def test_application_status_code(email):
    with allure.step('Подготовка тестовых данных'):
        url = "https://superjet.rostsayt.ru/"

        payload = {
            "E-mail": email
        }
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://superjet.rostsayt.ru',
            'priority': 'u=0, i',
            'referer': 'https://superjet.rostsayt.ru/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/141.0.0.0 Safari/537.36',
            'Cookie': 'message=%D0%92%D0%B0%D1%88%D0%B5%20%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B5%20'
                      '%D1%83%D1%81%D0%BF%D0%B5%D1%88%D0%BD%D0%BE%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5'
                      '%D0%BD%D0%BE%21 '
        }

    with allure.step(f'Вызов метода {url}'):
        response = requests.request("GET", url, headers=headers, data=payload)
    with allure.step('Проверка статус кода заявки'):
        assert response.status_code == 200, f'Статус код не равен 200, а равен {response.status_code}'




