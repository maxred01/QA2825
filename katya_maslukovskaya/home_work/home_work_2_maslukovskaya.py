import requests

url="https://swapi.dev/api/planets/3/"
response = requests.request("GET", url)
response_json=response.json()
assert response_json['population']=='1000',f'Популяция не равно 1000, а равно {response_json['population']}'
assert response_json['created']=='2014-12-10T11:37:19.144000Z',f'Поле создано не соответствует.Должно быть {response_json['created']}'