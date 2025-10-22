import requests

url = "https://swapi.dev/api/people/1"

response = requests.request("GET", url)
response_json = response.json()

print(response_json)
assert response.status_code == 200, f'Статус код не равен 200. Статус код равен {response.status_code}'

assert 'name' in response_json, 'Ключа name нет в словаре'
assert 'height' in response_json, 'Ключа height нет в словаре'

assert response_json['height'] == "172", f'Рост {response_json["name"]} не равен 172, a равен {response_json["height"]}'
assert response_json['mass'] == "77", f'Вес {response_json["name"]} не равен 77, а равен  {response_json["mass"]}'
assert response_json['eye_color'] == 'blue', f'Цвет глаз {response_json["name"]} голубой, а {response_json["eye_color"]}'

assert 'https://swapi.dev/api/films/1/' in response_json['films'][0]

assert len(response_json['species']) == 0
