import pytest
import requests
import json

@pytest.mark.parametrize("email,password,expected_status", [
    ("eve.holt@reqres.in", "pistol", 200),
    ("test@example.com", "kfjfnn@125", 400),
    ("", "pistol", 400),
    ("eve.holt@reqres.in", "", 400),
])
def test_registration_status_codes(email, password, expected_status):


    URL = "https://reqres.in/api/register"

    payload = json.dumps({
        "email": email,
        "password": password
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'x-api-key': 'reqres-free-v1',
        'Cookie': '_gid=GA1.2.1025150496.1761548507; _ga_CESXN06JTW=GS2.1.s1761548507$o1$g0$t1761548507$j60$l0$h0; _ga=GA1.1.2073151058.1761548507; _ga_WSM10MMEKC=GS2.2.s1761548508$o1$g0$t1761548508$j60$l0$h0; __stripe_mid=28dcd931-b895-4944-a89c-0957fe202dcf0b7d5e'
    }

    response = requests.request('POST', URL, headers=headers, data=payload)

    response_json = response.json()

    assert response.status_code == expected_status, (
        f"Ожидался статус {expected_status}, но получен {response.status_code}\n"
        f"Email: {email}, Password: {password}"
    )

    print(f"Статус код корректный: {response.status_code} для email='{email}'")


