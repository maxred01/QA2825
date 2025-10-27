import requests
import json
from datetime import datetime, timezone
import pytest

@pytest.mark.parametrize("email", [None,
                                   "peter@12673",
                                   "peter@",
                                   "peter",
                                   "@klaven",
                                   "1267389",
                                   " ",
                                   "",
                                   " peter@klaven",
                                   "peter@klaven ",
                                   "peter @klaven",
                                   "peter @klaven ",
                                   ])
def test_api_post():
  time = datetime.now(timezone.utc)
  format_time = time.isoformat(timespec='milliseconds').replace("+00:00", "Z")

  url = "https://reqres.in/api/login"
  name = 'morpheus'
  job = 'leader'
  status_code = 400

  payload = json.dumps({
    "name": name,
    "job": job,
    "email": email
  })

  headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-api-key': 'reqres-free-v1'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  # response_json = response.json()

  # assert response.json()['name'] == name, f'name  field isn\'t {name}, it\'s {response.json()["name"]}'
  # assert type(response.json()['id']) == str, f'"id" is not a string, it\'s {type(response.json()["id"])}'
  # assert response.json()['createdAt'] == str(format_time), f'Поле имя не равно {format_time}, равно {response.json()["createdAt"]}'

  # assert response.status_code == status_code, f'Статус код не равен {status_code}, а равен {response.status_code}'
  assert response.json()['error'] == 'Missing password', 'Неверный текст ошибки'






