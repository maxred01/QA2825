import requests
import json
import pytest

@pytest.mark.parametrize("url, expected_status_code", [
    ("https://reqres.in/api/users?delay=3", 200),
    ("https://reqres.in/api/users?delay=3", 400),
    ("https://reqres.in/api/users?delay=3", 401),
    ("https://reqres.in/api/users?delay=3", 500),
])

def test_status_code(url, expected_status_code):

    url = "https://reqres.in/api/users?delay=3"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1',
        'Cookie': '_ga_CESXN06JTW=GS2.1.s1761556198$o1$g0$t1761556198$j60$l0$h0; _ga=GA1.2.1438090834.1761556199; _gid=GA1.2.945876708.1761556199; _ga_WSM10MMEKC=GS2.2.s1761556199$o1$g0$t1761556199$j60$l0$h0; __stripe_mid=af0c24c7-64d7-40ce-bc3f-a8dfdecae4a6f69ac7',

    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}, а равен {response.status_code}'


def test_data_length():

    url = "https://reqres.in/api/users?delay=3"
    response = requests.request("GET", url)

    assert len("data") > 1, f'В параметре data - {len("data")} элемента списка'




