import pytest, json, requests, allure



@allure.title(f'Апи тесты сайта zrobim.by')
@allure.story(f'Проверка статус кода отправки запроса анкеты соискателя')

def test_applicant_questionnaire():

    url = "https://zrobym.bitrix24.by/bitrix/services/main/ajax.php?action=crm.site.form.fill"

    with allure.step("Подготовка тестовых данных"):

        payload = json.dumps({'properties': '{}',
                   'consents': '{"AGREEMENT_7":"Y"}',
                   'recaptcha': 'undefined',
                   'yandexSmartCaptcha': 'undefined',
                   'timeZoneOffset': '-180',
                   'values': '{"CONTACT_NAME":["Karl"],"CONTACT_LAST_NAME":["Franz"],"CONTACT_POST":["Engineer"],"LEAD_LINK":["https://bntu.by/index.php/news/3036-ya-inzhener"],"CONTACT_PHONE":["+375 (44) 693-55-66"],"CONTACT_EMAIL":["test_test@gmail.com"] '
                             })

        headers = {
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'origin': 'https://zrobim.by',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://zrobim.by/',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'Cookie': 'BITRIX_SM_kernel=-crpt-kernel_0; BITRIX_SM_kernel_0=ok4imn1EbsydSVVP1xKdu3R9f9y6urv17wE6tqHYnGZNbuNlp-zvYPceUm253heFjy9CiM7XPA_umjvFDN7NrPswqHt9rQqYKBVVnh4pbSjNUSwkLXTl46etFc8JOSRq-VVb3NIWmFLZV3sq673qAuJLx1n00rbfNruPa_UUnFqUm3RNlveMQS-WF-EPEiiHwgBUz5DCeLNu4g6T6UxoTA2giKRBg8o7IDcsstR-HmYoXHcQlIBDa0WRNTxQ_5VjzNHE58TJNp9Erhg_yE_q5t_68XjVPUB82uLI0xT-IwkbqEmXj6q9EaLpenOGEpxvcUULwgjyhm4DxBm7xF_IE44s1bFu0G5ShnRO5x-FlEQn28ocyXUD53-kDpgiAntO7tCbvBQGXKmTnpdtE3wOGTmxBON27Rf0JYB4Q5jItnSJ7Qm1mLfAy2v1jtpFcJkSlBBd3Cm7xbg_DIbCuM6tBITCL4qWlwmSmns4ddAcNQOBq49879eyW_3b84mILB-s-3V9O1GW9Pu8VgbXqgrqVPdYg_OXPNZ78aCx0Z4A9id8xY1yEyksQEY4G-Dlde5EtRXauMBEf5ygyCLxKNLWhobrLgwzVpE15Bn1-rOqJZOHfbDZ3hLBNeGdZnizBNRvU5X6ppPtuULm6obZN3lvxREmGiyXb1nHMoqJ45VNprKBOcID7R5GOE0YI3eUkcfrb64y88x02oCQOCgMvr0Tvhl9Pd6MsDBwLHs; qmb=0.'
        }


    with allure.step(f"Выполнение POST-запроса к {url}"):

        response = requests.request("POST",url, json=payload, headers=headers, data=payload)

    with allure.step("Проверка статус кода и тела ответа"):

        assert response.status_code == 200, f'Статус код не равен 200. Статус код равен {response.status_code}. Ответ: {response.text}'


