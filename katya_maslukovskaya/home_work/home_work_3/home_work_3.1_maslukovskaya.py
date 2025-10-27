import requests
import json

url = "https://reqres.in/api/users?delay=3"

payload = json.dumps({
  "email": "peter@klaven"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-origin',
  'Accept-Language': 'ru',
  'Sec-Fetch-Mode': 'cors',
  'Accept-Encoding': 'gzip, deflate, br',
  'Origin': 'https://reqres.in',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
  'Referer': 'https://reqres.in/',
  'Content-Length': '24',
  'Connection': 'keep-alive',
  'Host': 'reqres.in',
  'Sec-Fetch-Dest': 'empty',
  'Cookie': '__stripe_mid=eadd9358-eaf3-4a00-b63c-03cd8eef0b47fd91bb; _ga=GA1.1.166543595.1761151398; _ga_CESXN06JTW=GS2.1.s1761151398$o1$g0$t1761151398$j60$l0$h0; _ga_WSM10MMEKC=GS2.2.s1761151398$o1$g0$t1761151398$j60$l0$h0; _gid=GA1.2.1219093962.1761151398',
  'x-api-key': 'reqres-free-v1'
}

response = requests.request("POST", url, headers=headers, data=payload)

assert response.status_code==200,f'Статус код не равен 200,а {response.status_code}'
assert len(response.json()['data'])>1, f'В ответе параметра менее 1 элемента'