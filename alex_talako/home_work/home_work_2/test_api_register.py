import requests
import json
import pytest



@pytest.mark.parametrize("url, expected_status_code", [
    ("https://reqres.in/api/register", 301),
    ("https://reqres.in/api/register", 404),
    ("https://reqres.in/api/register", 200),
    ("https://reqres.in/api/register", 102),
])
def test_status_code(url, expected_status_code):
    url = "https://reqres.in/api/register"
    payload = json.dumps({
    "email": "eve.holt@reqres.in",
    "password": "pistol",
    })
    headers = {
      'accept': '*/*',
      'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/json',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
      'x-api-key': 'reqres-free-v1',
      'Cookie': '__stripe_mid=53efb1d0-f3de-47ee-9ac8-07eaeb66bfc645de81; _gid=GA1.2.1105458401.1761503381; _ga_CESXN06JTW=GS2.1.s1761503380$o2$g0$t1761503380$j60$l0$h0; _ga=GA1.1.2138524702.1761315586; _ga_WSM10MMEKC=GS2.2.s1761503381$o2$g0$t1761503381$j60$l0$h0'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == expected_status_code,f'Статус код должен быть равен {response.status_code}'

    print(response.json())

@pytest.mark.parametrize("expected_id,expected_token",[
    (1,"asdasd"),
    (2,""),
    (None,"21312"),
    (4,"QpwL5tke4Pnpja7X4"),
])
def test_id_and_token(expected_id,expected_token):

    payload = json.dumps({
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    })
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'x-api-key': 'reqres-free-v1',
        'Cookie': '__stripe_mid=53efb1d0-f3de-47ee-9ac8-07eaeb66bfc645de81; _gid=GA1.2.1105458401.1761503381; _ga_CESXN06JTW=GS2.1.s1761503380$o2$g0$t1761503380$j60$l0$h0; _ga=GA1.1.2138524702.1761315586; _ga_WSM10MMEKC=GS2.2.s1761503381$o2$g0$t1761503381$j60$l0$h0'
    }
    url = "https://reqres.in/api/register"
    response = requests.request("POST", url, headers=headers, data=payload)

    assert "id" in response.json(),f'Параметр id отсутствует'
    assert "token" in response.json(),f'Параметр token отсутствует'
    assert response.json()['id'] == expected_id
    assert response.json()['token'] == expected_token