import requests

url="https://swapi.dev/api/planets/3/"


response = requests.request("GET", url)
response_json=response.json()


assert response_json['population']=='1000',f'Популяция не равно 1000, а равно {response_json['population']}'
assert response_json['created']=='2014-12-10T11:37:19.144000Z',f'Поле создано не соответствует.Должно быть {response_json['created']}'
assert response_json['residents']==[]
assert response_json['url']=='https://swapi.dev/api/planets/3/',f'Поле url не соответствует'
assert 'gravity' in response_json, f'Поля gravity нет в ответе'
assert 'residents' in response_json, f'Поля residents нет в ответе'
assert isinstance(url,str),f'Поле url не является строкой'
assert response.status_code==200,f'Статус код не равен 200,а {response.status_code}'