import requests
import pytest
import allure

BASE_URL = "https://zrobim.by"

ENDPOINT = "/zrobym.bitrix24.by/bitrix/services/main/ajax.php?action=crm.site.form.fill"


sql_payloads = [
    "'",
    " OR '1'='1",
    "' OR '1'='1' --",
    "\" OR \"1\"=\"1\" --",
    ";",
    "UNION SELECT NULL, NULL, NULL"
]

@allure.title(f'Апи тесты сайта zrobim.by')
@allure.story(f'Проверка на базовую SQL-инъекцию через параметры URL')

@pytest.mark.parametrize("payload", sql_payloads)
def test_sql_injection_url_parameter(payload):


    url_with_payload = f"{BASE_URL}{ENDPOINT}?id={payload}"

    try:
        response = requests.get(url_with_payload, timeout=10)

        # Проверки:
        # 1. Код ответа не должен быть 500 (Internal Server Error)
        assert response.status_code != 500, f"Получена ошибка сервера (500) с payload: {payload}"

        # 2. В теле ответа не должно быть сообщений об ошибках БД
        assert "syntax error" not in response.text.lower(), f"Обнаружена синтаксическая ошибка БД с payload: {payload}"
        assert "sql error" not in response.text.lower(), f"Обнаружена ошибка SQL с payload: {payload}"
        assert "database error" not in response.text.lower(), f"Обнаружена ошибка базы данных с payload: {payload}"


        # Если API защищено, оно должно вернуть 400 Bad Request, 403 Forbidden или 404 Not Found.
        print(f"Payload '{payload}' обработан корректно (Status: {response.status_code})")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Произошла ошибка при запросе с payload: {payload}. Ошибка: {e}")


