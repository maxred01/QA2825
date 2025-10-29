
import pytest, json, requests, allure


@allure.title('Апи тесты')
@allure.story('Проверка статус кода')

def test_api_post():
    with allure.step("Подготовка тестовых данных"):
        url = "https://zrobim.by/"

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'Cookie': 'evo1fyfmeo=1474911d737971bffb695f36c0359896; _ga=GA1.2.325109144.1761589531; _gid=GA1.2.1923805305.1761589531; _ym_uid=1761589531944854201; _ym_d=1761589531; _ym_isad=2; _ym_visorc=w; _ga_KZZDLHXL9F=GS2.1.s1761589530$o1$g0$t1761589530$j60$l0$h0; _ga_KZF9GJ956X=GS2.1.s1761589530$o1$g0$t1761589530$j60$l0$h0'
        }
    with allure.step("Вызов метода api "):
        response = requests.request("GET", url, headers=headers)

    with allure.step("Проверка статус кода "):
        assert response.status_code == 200, f'Статус код не равен 200. Статус код равен {response.status_code}'

