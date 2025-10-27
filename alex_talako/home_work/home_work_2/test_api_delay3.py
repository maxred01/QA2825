import requests
import json
import pytest



@pytest.mark.parametrize("url, expected_status_code", [
    ("hhttps://reqres.in/api/users?delay=3", 203),
    ("https://reqres.in/api/users?delay=3", 404),
    ("https://reqres.in/api/users?delay=3", 200),
    ("https://reqres.in/api/users?delay=3", 100),
])
def test_status_code(url, expected_status_code):


    payload = {}
    headers = {
      'accept': '*/*',
      'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/json',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
      'x-api-key': 'reqres-free-v1',
      'Cookie': '__stripe_mid=53efb1d0-f3de-47ee-9ac8-07eaeb66bfc645de81; _gid=GA1.2.1105458401.1761503381; _ga_CESXN06JTW=GS2.1.s1761557463$o5$g0$t1761557463$j60$l0$h0; _ga=GA1.1.2138524702.1761315586; _ga_WSM10MMEKC=GS2.2.s1761557464$o4$g0$t1761557464$j60$l0$h0'
    }
    url = "https://reqres.in/api/users?delay=3"
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == expected_status_code, f'Статус код должен быть равен {response.status_code}'

def test_data_length():
    url = "https://reqres.in/api/users?delay=3"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'if-none-match': 'W/"600-DSziLS3KlRfI5T2Av9pzclJLaQk"',
        'priority': 'u=1, i',
        'referer': 'https://reqres.in/',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'x-api-key': 'reqres-free-v1',
        'Cookie': '__stripe_mid=53efb1d0-f3de-47ee-9ac8-07eaeb66bfc645de81; _gid=GA1.2.1105458401.1761503381; _ga_CESXN06JTW=GS2.1.s1761557463$o5$g0$t1761557463$j60$l0$h0; _ga=GA1.1.2138524702.1761315586; _ga_WSM10MMEKC=GS2.2.s1761557464$o4$g0$t1761557464$j60$l0$h0'
        }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert len('data') > 1, f'Количество элементов в data равно {len("data")}'