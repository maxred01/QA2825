import requests

url = "https://swapi.dev/api/people/1"
response = requests.request("GET", url)
response_json=response.json()

print(response_json)
assert 'name' in response_json, 'параметра нет в ответе'
#assert 'height' in response_json, 'параметра нет в ответе'
#assert response_json['height']=="172",f'Рост{response_json["name"]}не равен 172, а равен {response_json['height']}'

#assert response_json['name']=="Luke Skywalker",f'Имя{response_json['name']}, а не {response_json["name"]} '
#assert response_json['mass']=="77",f'Вес{response_json["name"]}не равен 7, а не {response_json['mass']}'
#assert response_json['eye_color']=="lue",f'Цвет глаз{response_json["name"]}не равен lue, а не {response_json['eye color']}'

#assert response_json[list("Films"()),[0]]=="https://swapi.dev/api/films/2/", f'Запрос {response_json["films",0]} не валидный, а равен {response_json["films"]}'


#assert 'https://swapi.dev/api/films/2/' in response_json['films'][0]
assert response_json['species']==[]
