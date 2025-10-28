import requests

url = "https://swapi.dev/api/planets/3/"
response = requests.request("GET", url)
response_json = response.json()

print(response_json)

# '1. Проверка статус кода'

assert response.status_code == 200,f'Статус код равен 200, а должен быть равен {response.status_code}'

# '2. Проверка, что в ответе есть поля: gravity, residents'

assert 'gravity' in response_json and 'residents' in response_json, 'Параметр(ы)  отсутствует(ют)'
assert 'gravity' in response_json, 'Параметр отсутствует'
assert 'residents' in response_json, 'Параметр отсутствует'

# '3. Проверка, что значение в поле равно ожидаемому. Для полей: url, created'

assert response_json['url'] == "https://swapi.dev/api/planets/3/", f'Значение в поле url равен "https://swapi.dev/api/planets/3/, а должен быть равен {response_json["url"]}'

assert response_json['created'] == "2014-12-10T11:37:19.144000Z", f'Значение в поле created равен "2014-12-10T11:37:19.144000Z", а должен быть равен {response_json["created"]}'

# '4. Проверка, что значение поля url имеет тип данных str'

assert type(response_json['url']) == str,f'Значение поля типа данных url указано str, а тип данных должен быть {type(response_json["url"])}'
assert isinstance(response_json['url'],str),f'Значение поля типа данных url указано str, а тип данных должен быть {type(response_json["url"])}'