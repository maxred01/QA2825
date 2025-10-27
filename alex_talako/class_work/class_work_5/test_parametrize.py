import random

import pytest
import requests
import json
import allure


@pytest.mark.parametrize('input, expected', [(1,2),(2,3),(3,4)])
def test_increment_function(input, expected):
    assert input + 1 == expected

# import pytest
# @pytest.mark.parametrize("input", range(5))
# def test_square_function(input):
#   assert input ** 2 == input * input

# def generate():
#     return random.randint(1,6)



@allure.title('Проверка api теста')
@allure.story('Проверка api теста 1')
@allure.feature('Проверка api теста 2')
@pytest.mark.parametrize("page, data, message", [(1,6, 'Тест успешный'),(1, 3,'Тест неуспешный'),(1,5, 'Тест неуспешный')])
def test_api_post(page, data, message):
    with allure.step('Подготовка тестовых данных '):
        url = "https://reqres.in/api/users?delay=3"
        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Accept-Language': 'ru',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
            'Cookie': '__stripe_mid=eadd9358-eaf3-4a00-b63c-03cd8eef0b47fd91bb; __stripe_sid=21f54d81-93b7-449d-be2d-7b4bd8720e5d58bcb0; _ga=GA1.1.166543595.1761151398; _ga_CESXN06JTW=GS2.1.s1761151398$o1$g0$t1761151398$j60$l0$h0; _ga_WSM10MMEKC=GS2.2.s1761151398$o1$g0$t1761151398$j60$l0$h0; _gid=GA1.2.1219093962.1761151398',
            'x-api-key': 'reqres-free-v1'}
    with allure.step('Вызов метода api/users?delay=3'):
        response = requests.request("GET", url, headers=headers)
    with allure.step('Проверка поля page'):
        assert response.json()['page'] == page, message
    with allure.step('Проверка поля data'):
        assert len(response.json()['data']) == data, message
