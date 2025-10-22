import requests

url = "https://swapi.dev/api/planets/3/"
response = requests.request("GET", url)
response_json = response.json()

print(response_json)

#1. Проверка статуса кода

assert response.status_code == 200,f'Статус кода {response.status_code}'

#2. Проверка, что в ответе есть поля: gravity, residents

assert 'gravity' in response_json, 'Параметр gravity отсутствует'
assert 'residents' in response_json, 'Параметр residents отсутвует'

#3.Проверка , что значение в поле равно ожидаемому. Для полей: url, created

assert 'https://swapi.dev/api/planets/3/' in response_json['url'], 'Ожидаемое значение в поле url отсутствует'
assert '2014-12-10T11:37:19.144000Z' in response_json['created'],'Ожидаемое значение в поле created отсутствует'

#4.Проверка, что значение поля url имеет тип данных str

assert type(response_json['url']) == str,'В поле url тип данных не str'