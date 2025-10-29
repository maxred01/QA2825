import pytest, json, requests, random, allure

def generate():
    return random.randint(1, 6)

@allure.title ("Проверка апи теста")
@allure.story ("Проверка апи теста1")
@allure.feature ("Проверка апи теста2")
@pytest.mark.parametrize("page, data, message", [(1, 6, 'тест успешный'), (1, 3, 'тест неуспешный'), (1, 5, 'Тест неуспешный')])
# @pytest.mark.parametrize("page, data", [(1, 6),pytest.param(1, generate()), (1, 5)])
# @pytest.mark.parametrize("page, data", [(1, 6),pytest.param(1, 6, marks=pytest.mark.xfail), (1, 5)])
def test_api_post(page, data, message):
    with allure.step("Подготовка тестовых данных"):
        url = "https://reqres.in/api/users?delay=3"

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36',
            'x-api-key': 'reqres-free-v1',
            'Cookie': '__stripe_mid=ef8e35d8-2039-4ea5-b3d0-9508fae52aeeceb381; _ga_CESXN06JTW=GS2.1.s1761158214$o2$g1$t1761158215$j59$l0$h0; _ga=GA1.1.644500490.1761151719; _ga_WSM10MMEKC=GS2.2.s1761158216$o2$g0$t1761158216$j60$l0$h0'
        }
    with allure.step('Вызов метода api/api/users?delay=3'):
        response = requests.request("GET", url, headers=headers)

    with allure.step('Проверка поля page'):
        assert response.json()['page'] == page,message
    with allure.step('Проверка поля data'):
        assert len(response.json()['data']) == data, message
    # assert response.json()['page'] == page, f'Получено неверное количество элементов. Получено {response.json()["page"]}, вместо {page}'
    # assert len(response.json()['data']) == data, f'Получено неверное число элементов. Получено {response.json()["data"]}, вместо {data}'