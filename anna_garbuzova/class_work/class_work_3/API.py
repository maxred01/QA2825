import requests
import json

url = "https://swapi.dev/api/people/1"
response = requests.request("GET", url)
response_json = response.json()

print(response_json)
assert 'name' in response_json, "Параметр 'name' отсутствует"
assert 'height' in response_json, 'Параметр рост отсутствует'
assert 'mass' in response_json, 'Параметр вес отсутвует'

assert response_json['height'] == '172', f'Рост {response_json['name']} не равен 172, а равен {response_json["height"]}'
assert response_json['name'] == 'Luke Skywalker',f'Его имя не {response_json["name"]}, а Luke Skywalker'
assert response_json['mass'] == '77', f'Вес {response_json['name']} не равен 77, а равен {response_json["mass"]}'
assert response_json['eye_color'] == 'blue', f'У{response_json['name']} не голубой, а его цвет глаз {response_json["eye_color"]}'

assert 'films' in response_json, 'Праметр films отстутствует'
assert response_json['films'] [0] == 'https://swapi.dev/api/films/1/', 'Элемент списка отстутствует'
assert 'https://swapi.dev/api/films/1/' in response_json['films'] [0]

assert not response_json['species'], 'Список не пуст'
assert len(response_json['species']) == 0