import pytest, json, requests, allure


@allure.title(f'Апи тесты сайта')
@allure.story(f'Проверка статус кода сайта')

def test_api_post():
    with allure.step("Подготовка тестовых данных"):
        url = "https://zrobim.by/"

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'Cookie': 'evo1fyfmeo=1474911d737971bffb695f36c0359896; _ga=GA1.2.325109144.1761589531; _gid=GA1.2.1923805305.1761589531; _ym_uid=1761589531944854201; _ym_d=1761589531; _ym_isad=2; _ym_visorc=w; _ga_KZZDLHXL9F=GS2.1.s1761589530$o1$g0$t1761589530$j60$l0$h0; _ga_KZF9GJ956X=GS2.1.s1761589530$o1$g0$t1761589530$j60$l0$h0'
        }
    with allure.step("Вызов метода api/zrobim.by/"):
        response = requests.request("GET", url, headers=headers)

    with allure.step("Проверка статус кода "):
        assert response.status_code == 200, f'Статус код не равен 200. Статус код равен {response.status_code}'

@allure.title(f'Апи тесты ссылок на сайте')
@allure.story(f'Проверка статус кода всех ссылок на сайте')

@pytest.mark.parametrize("status_code, url, name", [
(200,"https://int.design/en/project/k-17","K17 SILVER WINNER GR"),
(200,"https://winners.architizer.com/2025/Vision/architectural-concept/vision-for-landscape/","Architizer Vision Aw"),
(200,"https://zrobim.by/",""),
(200,"https://architectureprize.com/winners/winner.php?id=8990&mode=hm&compID=12810","Matski House Honorab"),
(200,"https://archello.com/news/archello-awards-2025-longlist-projects","Archello Awards 2025"),
(200,"https://frameweb.com/?modus=search&filters=W3sidHlwZSI6ImtleXdvcmQiLCJ2YWx1ZSI6Inpyb2JpbSIsImNhdGVnb3J5IjoienJvYmltIn1d","Winners of the month"),
(200,"https://ad-c.org/winner/matski-house-gold-winner-custom-dwelling-design-iada-2024/","Gold Winner of the I"),
(200,"https://retailawards.by/news/pobediteli-i-laureaty-premii-belarus-retail-real-estate-awards-2024/","Р›СѓС‡С€РµРµ РѕС„РѕСЂРјР»РµРЅРёРµ РѕС„"),
(200,"https://archnovation.ru/","Р›СѓС‡С€РёР№ РїСЂРѕРµРєС‚ РіСЂР°РґРѕВ­")
]
                         )


def test_link(status_code, url, name):
    with allure.step(f"Подготовка тестовых данных для api {name}"):
        url = "https://zrobim.by/"

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'Cookie': 'evo1fyfmeo=1474911d737971bffb695f36c0359896; _ga=GA1.2.325109144.1761589531; _gid=GA1.2.1923805305.1761589531; _ym_uid=1761589531944854201; _ym_d=1761589531; _ym_isad=2; _ym_visorc=w; _ga_KZZDLHXL9F=GS2.1.s1761589530$o1$g0$t1761589530$j60$l0$h0; _ga_KZF9GJ956X=GS2.1.s1761589530$o1$g0$t1761589530$j60$l0$h0'
        }
    with allure.step(f"Вызов метода {url} "):
        response = requests.request("GET", url, headers=headers)

    with allure.step(f"Проверка статус кода ссылок на сайте"):
        assert response.status_code == status_code, f'Статус код не равен 200. Статус код равен {response.status_code}'