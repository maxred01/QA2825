import json
import requests
import pytest


@pytest.mark.parametrize('email',[None,
                                  'peter@klaven'
                                  'peterv  @klaven',
                                  'pet324er@klaven',
                                  '@klaven',
                                  'peter@klaven',
                                  ])
def test_api_post(email):
    URL = 'https://reqres.in/api/uesrs?delay=3"

  from datetime import datetime,timezone
  time=datetime.now(timezone.utc)
  format_time=time.isoformat(timespec='milliseconds').replace("=00:00","Z")

  #def is_correct_format(time):
  #    return bool(re.match(r'^\d{4}-\d{2}'),time)
  #print(is_correct_format())


  #name='Оля'
  #job='кассир'
  error='missing password'
  email='peter@klaven'

  payload = json.dumps=({
      "email": email,
  #    "job": job
  })
  headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
    'Cookie': '__stripe_mid=eadd9358-eaf3-4a00-b63c-03cd8eef0b47fd91bb; __stripe_sid=21f54d81-93b7-449d-be2d-7b4bd8720e5d58bcb0; _ga=GA1.1.166543595.1761151398; _ga_CESXN06JTW=GS2.1.s1761151398$o1$g0$t1761151398$j60$l0$h0; _ga_WSM10MMEKC=GS2.2.s1761151398$o1$g0$t1761151398$j60$l0$h0; _gid=GA1.2.1219093962.1761151398',
    'x-api-key': 'reqres-free-v1'
  }


  response=requests.request('POST',URL,headers=headers,data=payload)

  #assert response.status_code==201,f'Статус код не равен 201, а равен {response.status_code}'
  #assert isinstance(id,str),f'Поле id не является строкой'
  #assert response.json()['name']==name,f'Поле имя не равно {name}, а равно {response.json()['name']}'
  #assert response.json()['createdAt']==str(format_time),f'Поле имя не равно {format_time}, а равно {response.json()['createdAt']}'

  #assert response.status_code==400,f'Статус код не равен 400, а равен {response.status_code}'
  #assert response.json()['error']=='missing password',f'Поле не соответствует'
