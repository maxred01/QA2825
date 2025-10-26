import json
import requests

from datetime import datetime,timezone

time = datetime.now(timezone.utc)
format_time = time.isoformat(timespec='milliseconds').replace('+00:00','Z')

URL = "https://reqres.in/api/users"
name = 'Аня'
job = 'Кассир'

playload = json.dumps( {
    "name": name,
    "job": job
        })

headers = {
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Accept-Language': 'ru',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
  'Cookie': '__stripe_mid=eadd9358-eaf3-4a00-b63c-03cd8eef0b47fd91bb; __stripe_sid=21f54d81-93b7-449d-be2d-7b4bd8720e5d58bcb0; _ga=GA1.1.166543595.1761151398; _ga_CESXN06JTW=GS2.1.s1761151398$o1$g0$t1761151398$j60$l0$h0; _ga_WSM10MMEKC=GS2.2.s1761151398$o1$g0$t1761151398$j60$l0$h0; _gid=GA1.2.1219093962.1761151398',
  'x-api-key': 'reqres-free-v1'
}
RESPONSE = requests.request("POST", URL, headers = headers, data = playload)

print(RESPONSE.text)

assert RESPONSE.json()['name'] == name, f'Поле имя не равно {name}, а равно {RESPONSE.json()["name"]}'
assert RESPONSE.status_code == 201, f'Status code: {RESPONSE.status_code}'
assert RESPONSE.json()['name'] == 'morpheus', f'Имя morpheus, а не {RESPONSE.json()['name']}'
assert type(RESPONSE.json()['id']) == str,'В поле id тип данных не str'
assert RESPONSE.json()['createdAt'] == str(format_time), f'Поле CreatedAt не равно {format_time}, а равно {RESPONSE.json()['createdAt']}'


