import requests
import json
import pytest


@pytest.mark.parametrize("email", [None,
                                   "peter@1234",
                                   "peter@",
                                   "peter",
                                   "@klaven",
                                   "12342",
                                   " ",
                                   "",
                                   " peter@klaven",
                                   "peter@klaven ",
                                   "peter @klaven ",
                                   ])
def test_api_post(email):
  url = "https://reqres.in/api/login"

  payload = json.dumps({
    "email": email,
  })

  headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-api-key': 'reqres-free-v1',
    'Cookie': '_gid=GA1.2.1967390961.1761150989; _ga_CESXN06JTW=GS2.1.s1761150988$o1$g0$t1761150988$j60$l0$h0; _ga=GA1.1.1187057280.1761150989; _ga_WSM10MMEKC=GS2.2.s1761150988$o1$g0$t1761150988$j60$l0$h0; __stripe_mid=d8b2c9c0-3d1e-45de-811c-816fb5563575689bdf; __stripe_sid=0c2ed8f0-6510-41e9-9e9c-3e3a7d0a118beb49ed'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  assert response.status_code == 200, 'Неверный статус код'
  assert response.json()['error'] == 'Missing password', 'Неверный текс ошибки'

