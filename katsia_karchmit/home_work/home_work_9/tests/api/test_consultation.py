import pytest, json, requests, allure



@allure.title(f'Апи тесты сайта zrobim.by')
@allure.story(f'Проверка статус кода отправки запроса на консультацию')

def test_consultation():

    url = "https://zrobim.by/thanks.html"

    with allure.step("Подготовка тестовых данных"):



        payload = {
            "your-name": "Test User",
            "city": "Minsk",
            "phone": "+375 (29) 123-45-67",
            "your-email": "testuser@example.com",
            "your-message": "Здравствуйте, хотел бы проконсультироваться по проекту."
        }


        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://zrobim.by',
            'Referer': 'zrobim.by',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
        }


    with allure.step(f"Выполнение POST-запроса к {url}"):

        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Проверка статус кода и тела ответа"):

        assert response.status_code == 200, \ f'Статус код не равен 200. Статус код равен {response.status_code}. Ответ: {response.text}'


