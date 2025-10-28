import requests

url = "https://swapi.dev/api/planets/3/"

response = requests.request("GET", url)

response_json = response.json()
print(response_json)

assert response.status_code == 200, f'Статус код не равен 200. Статус код равен {response.status_code}'

assert 'gravity' in response_json, 'Ключа gravity нет в словаре'
assert 'residents' in response_json, 'Ключа residents нет в словаре'

assert response_json['created'] == "2014-12-10T11:37:19.144000Z", f'Значение в поле created не равно 2014-12-10T11:37:19.144000Z. Значение в поле created равно {response_json['created']}'
assert response_json['url'] == 'https://swapi.dev/api/planets/3/', f'Значение в поле url не равно "https://swapi.dev/api/planets/3/". Значение в поле url равно {response_json['url']}'

assert type(response_json['url']) == str, f'Значение поля "url" не является типом данных str. Тип данных "url" равняется {type(response_json['url'])}'