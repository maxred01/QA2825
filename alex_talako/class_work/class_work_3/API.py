import requests

url = "https://swapi.dev/api/people/1"
response = requests.request("GET", url)
response_json = response.json()

print(response_json)
assert 'name' in response_json, 'Параметр отсутсвует'
# имя,масса и цвет глаз

# assert response_json['height'] == "172", f'Рост {response_json["name"]} не равен 172, а равен {response_json["height"]}'

# assert response_json['name'] == "Lukes Skywalker", f'Имя {response_json["name"]} не является нужным, а его значение {response_json ["name"]}'
# assert response_json['mass'] == "77", f'Масса {response_json["mass"]} не равна 77, а её значение {response_json ["mass"]}'
# assert response_json['eye_color'] == "red", f'Цвет глаз {response_json["eye_color"]} не верный, а его значение {response_json ["eye_color"]}'

# assert 'films' in response_json, 'Параметр отсутсвует'

# assert 'https://swapi.dev/api/films/1/' in response_json['films'][2], "Неверное значение"


assert response_json['species'] == "[]", 'Ошибка, там не должно быть значения'

# https://swapi.dev/