import pytest
import requests
import json
import random
import allure

@allure.title('Проверка статус кода главной страницы')
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

def test_code_status(url, expected_status_code):
  with allure.step('Подготовка тестовых данных'):
    url = "https://autogroup.by"
    headers = {
      'Cookie': 'PHPSESSID=acvq4aXawRnX8wIDDAbKIP3MUlpZh2XW'
}
  with allure.step('вызов url'):
    response = requests.request("GET", url, headers=headers)
  with allure.step('Проверка статус кода страницы'):
    assert response.status_code==403,f'Статус код не равен 200,а {response.status_code}'