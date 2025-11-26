import pytest,json,requests,random,allure

@allure.epic('API тесты')
@allure.story('Позитивные тесты')
@allure.feature('Консультация')
@pytest.mark.parametrize('url, expected_status_code',[
  ("https://autogroup.by",200),
  ("https://autogroup.by",403),
  ("https://autogroup.by/kitay/",200),
  ("https://autogroup.by/",200),
  ("https://autogroup.by/korea/",403),
  ("https://autogroup.by/europa/",401),
  ("https://autogroup.by/vin/",200),
  ("https://autogroup.by/usa/",200),
  ("https://autogroup.by/delivery-korea/",200)
  ])

def test_api_post(url, expected_status_code):
  with allure.step(f'подготовка тест данных для API'):
    url = "https://autogroup.by/#form-car-selection"

    headers = {
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Accept-Language': 'ru',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'no-cors',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://autogroup.by',
        'Content-Length': '0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
        'Referer': 'https://autogroup.by/',
        'Connection': 'keep-alive',
        'Host': 'mc.yandex.ru',
        'Sec-Fetch-Dest': 'empty',
        'Cookie': 'bh=YNP/iMgGaiHcytG2Abvxn6sE+taGzAjS0ZmQB/y5r/8H3/2r+A6mngI='
    }

  with allure.step('вызов метода https://autogroup.by/#form-car-selection'):
    response = requests.request("POST", url, headers=headers)


  with allure.step('проверка статус кода'):
    assert response.status_code==200,f'Статус код не равен 200,а {response.status_code}'