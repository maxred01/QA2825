import requests
import json

from pygments.lexers import data

url = "https://reqres.in/api/users?delay=3"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/json',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
  'x-api-key': 'reqres-free-v1',
  'Cookie': '_gid=GA1.2.1025150496.1761548507; _ga_CESXN06JTW=GS2.1.s1761548507$o1$g0$t1761548507$j60$l0$h0; _ga=GA1.1.2073151058.1761548507; _ga_WSM10MMEKC=GS2.2.s1761548508$o1$g0$t1761548508$j60$l0$h0; __stripe_mid=28dcd931-b895-4944-a89c-0957fe202dcf0b7d5e'
}

response = requests.request("GET", url, headers=headers, data=payload)

response_json = response.json()
data = response.json()

print(response_json)

#assert response.status_code == 200, f'Статус код не равен 300, а равен  {response.status_code}'

assert len(data["data"]) > 10, f'Expected more than 1 element, got {len(data["data"])}'