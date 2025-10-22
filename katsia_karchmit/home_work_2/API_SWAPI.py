import requests

url = "https://swapi.dev/api/planets/3/"

response = requests.request("GET", url)

response_json =response.json()

#assert "diameter" in response.json() , 'параметр diameter нет в ответе'

#assert response.json()["diameter"] == "10220", f'Диаметр {response_json["name"]} не равен 10220, а равен {response_json["diameter"]}'

assert len(response.json().get('residents',[])) == 0

#assert response.json()["residents"] == []
