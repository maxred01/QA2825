import requests
import json
from datetime import datetime, timezone

time = datetime.now(timezone.utc)
format_time = time.isoformat(timespec='milliseconds').replace("+00:00", "Z")

url = "https://reqres.in/api/users"
name = 'Максим'
job = 'Кассир'

payload = json.dumps({
  "name": name,
  "job": job
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

assert response.json()['name'] == name, f"Поле имя не равно {name}, а равно {response.json()['name']}"
assert response.json()['createdAt'] == str(format_time), f"Поле имя не равно {format_time}, а равно {response.json()['createdAt']}"

