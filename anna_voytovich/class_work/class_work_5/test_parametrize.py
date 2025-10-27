import random
import allure
import pytest
import requests

def generate():
    return random.randint(1, 6)
@allure.feature('Проверка апи тестов')
@pytest.mark.parametrize("page, data, message", [(1, 6, 'тест успешный'), (1, 3, 'тест неуспешен'), (1, 5, 'тест неуспешен')])
def test_increment_function(page, data, message):
    with allure.step('Подготовка тестовых данных '):
        url = "https://reqres.in/api/users?delay=3"
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1',
        'Cookie': '_ga_CESXN06JTW=GS2.1.s1761556198$o1$g0$t1761556198$j60$l0$h0; _ga=GA1.2.1438090834.1761556199; _gid=GA1.2.945876708.1761556199; _ga_WSM10MMEKC=GS2.2.s1761556199$o1$g0$t1761556199$j60$l0$h0; __stripe_mid=af0c24c7-64d7-40ce-bc3f-a8dfdecae4a6f69ac7'
    }
    with allure.step('Вызов метода api/users?delay=3 '):
        response = requests.request("GET", url, headers=headers)

    with allure.step('Подготовка поля page '):
        assert response.json()['page'] == page, message

    with allure.step('Подготовка поля date '):
        assert len(response.json()['data']) == data, message
