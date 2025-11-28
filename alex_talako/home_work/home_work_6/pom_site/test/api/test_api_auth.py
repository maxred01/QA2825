import pytest
import requests
import json
import allure


@allure.epic('API тест')
@allure.feature('Авторизация')
@allure.story('Негативный тест: Неверные учетные данные')
@allure.parent_suite('Tests for web interface')
@allure.suite('Tests for essential features')
@allure.sub_suite('Test for authentication')
@pytest.mark.parametrize("url, expected_status_code", [
    ("https://tryhackme.com/api/v2/auth/login", 403),

])
def test_api_login_invalid_credentials(url, expected_status_code):
    with allure.step(f'Подготовка тестовых данных и payload'):
        invalid_email = "nonexistent_user@example.com"
        invalid_password = "wrong_password123!"

        payload = json.dumps({
            "password": invalid_password,
            "email": invalid_email
        })

        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        }

    with allure.step(f'Вызов метода POST: {url} с неверными данными'):
        response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step(f'Проверка статус кода: {expected_status_code}'):
        assert response.status_code == expected_status_code, \
            f'Статус код не совпадает. Ожидался {expected_status_code}, получен {response.status_code}. ' \
            f'Ответ сервера: {response.text}'