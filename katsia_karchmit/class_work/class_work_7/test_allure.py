import pytest, json, requests, allure

@allure.epic("Апи тесты")
@allure.feature("Консультация")
@allure.story("Позитивные тесты")
@allure.title("Test консультация")
@allure.link("https://zrobim.by/", name="Website")
@allure.description("Отправка запроса на получение консультации")

def test_api_post():
    with allure.step("Подготовка тестовых данных"):
        url = "https://zrobim.by/"

        payload = 'formid=modal&name=TGHkldso&city=NJH&phone=86544895&email=tests%40test.mail.ru&comment=a%3F&org='

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://zrobim.by',
            'Referer': 'https://zrobim.by/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Cookie': '_ym_uid=1761589531944854201; _ym_d=1761589531; evo1fyfmeo=b8f9bfa982ad3c9a5dc4ea9a762b8aa8; _ym_visorc=w; _ym_isad=2; _gid=GA1.2.452976857.1761753958; _gat_gtag_UA_47383244_1=1; _ga=GA1.1.325109144.1761589531; _ga_KZZDLHXL9F=GS2.1.s1761753957$o2$g1$t1761755885$j58$l0$h0; _ga_KZF9GJ956X=GS2.1.s1761753957$o2$g1$t1761755885$j58$l0$h0'
        }
    with allure.step("Вызов метода"):
        response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step("Проверка статус кода "):
        assert response.status_code == 200, f'Статус код не равен 200. Статус код равен {response.status_code}'

