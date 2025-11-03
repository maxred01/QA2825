import allure
import pytest
import requests
import json



url = "https://superjet.rostsayt.ru/"


@allure.title('Проверка статус кода сайта')
@allure.story(f'Проверка статус кода сайта {url}')
@pytest.mark.parametrize("url, expected_status_code", [
    ("https://superjet.rostsayt.ru/", 200),
    ("https://superjet.rostsayt.ru/", 100),
    ("https://superjet.rostsayt.ru/", 400),
    ("https://superjet.rostsayt.ru/", 503),
    ("https://superjet.rostsayt.ru/", 104),
    ("https://superjet.rostsayt.ru/", 207),

])

def test_status_code(url, expected_status_code):
    with allure.step('Подготовка тестовых данных '):
        url = "https://superjet.rostsayt.ru/"

        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
        }
    with allure.step(f'Вызов метода {url} '):
        response = requests.request("GET", url, headers=headers, data=payload)
    with allure.step('Проверка статус кода '):
        assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}, а равен {response.status_code}'

@allure.title('Проверка статус кода ссылки на сайте')
@allure.story(f'Проверка статус кода всех ссылок на сайте {url}')
@pytest.mark.parametrize("status_code, url, label", [
    (200, "https://rostsayt.ru/", "Хочу такой же сайт"),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/25.jpg", ""),
    (200, "https://superjet.rostsayt.ru/#", ""),
    (200, "https://www.youtube.com/@krivov1", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/26.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/02.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/03.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/01.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/06.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/27.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/04.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/05.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/6.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/4.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/3.jpg", ""),
    (200, "https://vk.com/rost_sayt", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/1.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/10.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/11.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/9.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/7.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/14.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/15.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/13.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/12.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/19.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/18.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/17.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/16.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/23.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/22.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/21.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/24.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/28.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/20.jpg", ""),
    (200, "https://superjet.rostsayt.ru/#advantagers", "Преимущества"),
    (200, "https://superjet.rostsayt.ru/#effective", "Эффективность"),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/31.jpg", ""),
    (200, "https://superjet.rostsayt.ru/#comlpects", "Комплектация"),
    (200, "https://superjet.rostsayt.ru/#comforts", "Комфорт"),
    (200, "https://superjet.rostsayt.ru/#feedbacks", "Купить в лизинг"),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/32.jpg", ""),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/33.jpg", ""),
    (200, "https://superjet.rostsayt.ru/#advantagers", "Преимущества"),
    (200, "https://superjet.rostsayt.ru/#effective", "Эфективность"),
    (200, "https://superjet.rostsayt.ru/#comlpects", "Комплектации"),
    (200, "https://superjet.rostsayt.ru/#comforts", "Комфорт"),
    (200, "https://superjet.rostsayt.ru/assets/images/gallery/2k/new/29.jpg", ""),
    (300, "https://www.krivov.net/", "www.krivov.net"),
])

def test_links(status_code, url,label):
    with allure.step('Подготовка тестовых данных '):
        url = "https://superjet.rostsayt.ru/"

        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
        }
    with allure.step(f'Вызов метода {url} '):
        response = requests.request("GET", url, headers=headers, data=payload)
    with allure.step(f'Проверка статус кода ссылки на сайте {url}'):
        assert response.status_code == status_code, f'Статус код не равен {status_code}, а равен {response.status_code}'