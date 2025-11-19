import requests
import json
import pytest

@pytest.mark.parametrize("email", [None,
                                   "peter@klaven",
                                   "peter",
                                   "peter12@23klaven",
                                   "@peter@klaven",
                                   "@peterklaven",
                                   "",
                                   " ",
                                   "peter @klaven",
                                   ])
def test_api_post(email):
  #from datetime import datetime, timezone

  #time = datetime.now(timezone.utc)
  #format_time = time.isoformat(timespec='milliseconds').replace("+00:00", "Z")

  URL = 'https://reqres.in/api/login'


  payload = json.dumps({
    "email": email,
    })
  #name='Максим'
  #job="кассир"

  #payload = json.dumps({
   # "name": name,
    #"job": job
  #})
  headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-api-key': 'reqres-free-v1',
    'Cookie': '_gid=GA1.2.546223025.1761151299; __stripe_mid=f3ec9204-3e5c-411b-9206-38f6f5c0f82bae78cb; __stripe_sid=9a06f19a-8953-42cf-8f15-4717112a4bfec09f69; _ga_CESXN06JTW=GS2.1.s1761151298$o1$g1$t1761151706$j60$l0$h0; _ga=GA1.1.1173629549.1761151299; _ga_WSM10MMEKC=GS2.2.s1761151298$o1$g1$t1761151706$j60$l0$h0'
  }
  response = requests.request('POST', URL, headers=headers, data=payload)

  response_json = response.json()

  print(response_json)

  #assert response_json["name"] == name, f'Поле имя не равно {"name"}, а равно {response_json["name"]}'

  #assert response_json["createdAt"] == str(format_time), f'Поле имя не равно {"format_time"}, а равно {response_json["createdAt"]}'

  #assert type(response_json()["id"]) == str, f'Идентификатор {response_json["id"]} не строка'

  assert response_json["error"] == 'Missing password', 'Неверный текст ошибки'

  assert response.status_code == 400, 'Неверный статус код'


