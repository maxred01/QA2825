import pytest, json, requests, random, allure


@allure.feature('Апи тесты')
@allure.story('Проверка статус кода')
@pytest.mark.parametrize("status_code, url, name", [
    (403, "https://ozon.by/product/2286771799/", "403"),
    (403, "https://ozon.by/product/1456631237/", "403"),
    (403, "https://ozon.by/product/2033884956/", "403"),
    (403, "https://ozon.by/category/produkty-pitaniya-9200/", "РџСЂРѕРґСѓРєС‚С‹ РїРёС‚Р°РЅРёСЏ 403"),
    (403,
     "https://ozon.by/product/salfetki-ot-pyaten-na-odezhde-vlazhnye-pyatnovyvodyashchie-sredstvo-ochishchayushchie-obuv-mini-1650868905/?at=DqtDq8z32spKwY6yI59zYG2ujZQgrJHDB7lJnIWKBN1W",
     "Р Р°СЃРїСЂРѕРґР°Р¶Р° 11.11 403"),
    (403, "https://ozon.by/highlight/eshche-bolshe-tovarov-s-postoplatoy-3012403/", "403"),
    (403, "https://ozon.by/highlight/novye-kollektsii-3233777/", "403"),
    (403, "https://ozon.by/highlight/vau-tseny-2327694/", "403"),
    (403, "https://ozon.by/highlight/sdelano-v-belarusi-1541934/", "РЎРґРµР»Р°РЅРѕ РІ Р‘РµР»Р°СЂСѓСЃРё 4"),
    (403, "https://ozon.by/category/bytovaya-tehnika-10500/", "Р‘С‹С‚РѕРІР°СЏ С‚РµС…РЅРёРєР° 403")
]
                         )
def test_api_post(status_code, url, name):
    with allure.step(f'Подготовка тестовых данных для api {name}'):
        url = "https://reqres.in/api/users?delay=3"
        headers = {
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'x-api-key': 'reqres-free-v1',
            'Cookie': '_gid=GA1.2.1967390961.1761150989; _ga_CESXN06JTW=GS2.1.s1761150988$o1$g0$t1761150988$j60$l0$h0; _ga=GA1.1.1187057280.1761150989; _ga_WSM10MMEKC=GS2.2.s1761150988$o1$g0$t1761150988$j60$l0$h0; __stripe_mid=d8b2c9c0-3d1e-45de-811c-816fb5563575689bdf; __stripe_sid=0c2ed8f0-6510-41e9-9e9c-3e3a7d0a118beb49ed'
        }

    with allure.step(f'Вызов метода {url}'):
        response = requests.request("GET", url, headers=headers)

    with allure.step('Проверка статус кода'):
        assert response.status_code == status_code, f'Статус код не равен 200. Статус код равен {response.status_code}'
