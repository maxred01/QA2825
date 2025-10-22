import requests

url = "https://swapi.dev/api/people/1"

response = requests.request("GET", url)

response_json = response.json()



assert "name" in response_json, 'параметра name нет в ответе'

assert response_json["height"] == "172", f'Рост {response_json["name"]} не равен 172, а равен {response_json["height"]}'

assert response_json["mass"] == "77", f'Вес {response_json["name"]} не равен 77, а равен {response_json["mass"]}'

assert response_json["eye_color"] == "blue", f'Цвет глаз {response_json["name"]} не голубой, а равен {response_json["eye_color"]}'

assert "films" in response_json

assert 'https://swapi.dev/api/films/1/' in response_json['films'][0]

assert response_json["species"] == []