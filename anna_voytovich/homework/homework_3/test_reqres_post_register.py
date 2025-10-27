import requests
import json
import pytest



@pytest.mark.parametrize("url, expected_status_code", [
    ("https://reqres.in/api/register", 200),
    ("https://reqres.in/api/register", 400),
    ("https://reqres.in/api/register", 401),
    ("https://reqres.in/api/register", 405),
])

def test_status_code(url, expected_status_code):

    email = "eve.holt@reqres.in"
    password = "pistol"

    payload = json.dumps({
        "email": email,
        "password": password
    })
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1',
        'Cookie': '_ga_CESXN06JTW=GS2.1.s1761480385$o1$g0$t1761480385$j60$l0$h0; _ga=GA1.2.105275158.1761480386; _gid=GA1.2.522758497.1761480386; _ga_WSM10MMEKC=GS2.2.s1761480386$o1$g0$t1761480386$j60$l0$h0; __stripe_mid=c0d3b66b-037b-498f-b67d-c66a078da1f1dbc486; __stripe_sid=5060bb2a-8733-4d54-b657-a8b7259064b9b02937',
    }

    url = "https://reqres.in/api/register"

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}, а равен {response.status_code}'



@pytest.mark.parametrize("expected_id,expected_token",[
    (1,"dkomcoskmccs"),
    (2," "),
    (3,"12234456672"),
    (4,"QpwL5tke4Pnpja7X4"),
])
def test_id_and_token(expected_id,expected_token):

    email = "eve.holt@reqres.in"
    password = "pistol"
    payload = json.dumps({
        "email": email,
        "password": password,
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







