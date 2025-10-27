import requests
import json

url = "https://reqres.in/api/users?delay=3"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
  'content-type': 'application/json',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36',
  'x-api-key': 'reqres-free-v1',
  'Cookie': '__stripe_mid=ef8e35d8-2039-4ea5-b3d0-9508fae52aeeceb381; _ga_CESXN06JTW=GS2.1.s1761158214$o2$g1$t1761158215$j59$l0$h0; _ga=GA1.1.644500490.1761151719; _ga_WSM10MMEKC=GS2.2.s1761158216$o2$g0$t1761158216$j60$l0$h0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

assert response.status_code == 200, f'Status code is {response.status_code}'
assert len(response.json()['data']) > 1,'В параметре data 1 элемент или список пуст'
