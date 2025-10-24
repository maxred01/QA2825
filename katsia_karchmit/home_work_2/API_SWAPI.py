import requests

url = "https://swapi.dev/api/planets/3/"

response = requests.request("GET", url)

response_json =response.json()

print(response_json)

#Проверка статус кода

assert response.status_code == 200, f'Статус кода {response.status_code}'

#Проверка, что в ответе есть поля: gravity, residents

assert "gravity" in response.json() , 'параметр gravity нет в ответе'

assert "residents" in response.json() , 'параметр residents нет в ответе'

#Проверка, что значение в поле равно ожидаемому. Для полей: url, created

assert "https://swapi.dev/api/planets/3/" in response_json['url'], "Значение в поле url отсутствует"

assert '2014-12-10T11:37:19.144000Z' in response_json['created'], "Значение в поле created отсутствует"

#Проверка, что значение поля url имеет тип данных str

assert type(response_json['url']) == str,'В поле тип данных не str'
