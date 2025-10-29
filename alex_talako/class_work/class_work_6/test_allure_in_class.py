import requests
import json
import allure
import pytest


@allure.epic('API тесты')
@allure.feature('Авторизация')
@allure.story('Позитивные тесты')
@allure.parent_suite('Tests for web interface')
@allure.suite('Tests for essential features')
@allure.sub_suite('Test for authentication')
@pytest.mark.parametrize("url, expected_status_code" , [
    ("https://tryhackme.com/api/v2/auth/login", 200),
    ("https://tryhackme.com/api/v2/auth/login", 401),
    ("https://tryhackme.com/api/v2/auth/login", 582),
    ("https://tryhackme.com/api/v2/auth/login", 101),
    ("https://tryhackme.com/api/v2/auth/login", 203),
    ("https://tryhackme.com/api/v2/auth/login", 304),
])

def test_api_post(url, expected_status_code):
    with allure.step(f'Подготовка тестовых данных api'):
        url = "https://tryhackme.com/api/v2/auth/login"

        payload = json.dumps({
            "password": "dfjha!@214",
            "email": "test_test@gmail.com"
        })
        headers = {
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'baggage': 'sentry-environment=production,sentry-release=production-341f73a2f0,sentry-public_key=175180b5f191796714d2f9138c06c76a,sentry-trace_id=67a12b7edc574bb5aa5b41f155cb5932',
            'content-type': 'application/json',
            'csrf-token': 'aBJI9nIh-95n11lIU795qIG1xYF4FN3k__to',
            'origin': 'https://tryhackme.com',
            'priority': 'u=1, i',
            'referer': 'https://tryhackme.com/login',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sentry-trace': '67a12b7edc574bb5aa5b41f155cb5932-8c29c0ed84f0b77b',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'x-recaptcha-response': '0cAFcWeA68P8WyxxWEs0E07qS_ae2Kh_r_U1_57T_KVk57p-Hko0Uf6LtR-XVIVTr8mLNcsnUmZXyRcDTbRWQbFvSWMiWRfVikc885AEbELxjEIABm2l4DmNdAHGI0Z3XjeBAGwzoo-D7LcKVHemig1MX22bAHOxWex5sx9Er-NKy4FHY_sbgTiQ5gwFwc8sY4DftuPT-0yvWC3EZAvUot8J30H8uhFdrrGPyPW9j7C8Txu83SZ6HRBBxA53in1y6Pn78L8-N00iBg-LNsLfw35P0LFPSxWNb9fUAxMyDnOZoJWirDT0Y-3FVGZEOc0NZBSUOIvJaoynuDQJbO7Q4AmYSOl0sW-UH9UBY2DaIvsLIi6hc_hkVxYxFG5HJdWuCmoHEJknVfLZDi2ZU0X9hm7AYkWORKh1GvxgUNADYfrf6vHGrMXJCdRy6t1irZdmlpemKUIYXBeo6YgqknGF0LWbV0mI_ZFzQnAZLe5kUZo8oar0bRc47_TGKgb0htlWJyE5pxbnBHeFpDTWgeJJXPmN3aZHZDbzXt4DuUGVzLzL_XZLfyVAqqGftjMHMXJlhWHK2G73sBNGWsnem1jmKHTvBKNUYt0RhAkgQITPxAgT3WS6-bQ6YOgQEy10OCnuZ41iLbzGxONi4TtTcnRiFRkK0k5YOP8Uf7wQPpZHzShhn7TjEACkIR4Eh7-YtC_2FJPIkI2AnNRF3LgAZozxpEapHshT4-zSxDe1SZDoGJraO1XN4kL6f84jaVpXODo17StFQgpLdBkIIT',
            'Cookie': 'thm-aid=29ef4121-e713-4d07-b825-00be40a6a18c; _gcl_au=1.1.1404139791.1761589639; _hjSessionUser_1950941=eyJpZCI6IjliOTMyYzQxLTE4ODctNTc3My04ZjJjLWMzNWRjN2E2NGM2YiIsImNyZWF0ZWQiOjE3NjE1ODk2Mzg3NzUsImV4aXN0aW5nIjp0cnVlfQ==; ajs_anonymous_id=29ef4121-e713-4d07-b825-00be40a6a18c; _ga=GA1.1.1058267343.1761589639; _fbp=fb.1.1761589639155.592488567316109178; thm-amplitude-device-id=29ef4121-e713-4d07-b825-00be40a6a18c; hubspotutk=25b8762c6d7b33678b29531d55cc09a4; intercom-device-id-pgpbhph6=1ace7cda-b13c-47ef-a660-662960313f90; thm-amplitude-session-id=1761589639345; analytics_session_id=1761589639345; _csrf=FWqOtSU9yO9wyDoCiy0dCGZk; gbStickyBuckets__anonymousId||29ef4121-e713-4d07-b825-00be40a6a18c={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%2229ef4121-e713-4d07-b825-00be40a6a18c%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22google-one-tap-auto-login__0%22:%221%22%2C%22new-homepage__0%22:%221%22}}; cf_clearance=9vXych5gBKc55lbxEJMi5t2XH2eg.LDTM2qnPmILlAs-1761754551-1.2.1.1-eiIha_asOTrEJHG5R43u7KeKBKEFDteFAjXUa8ZOVNOWCe0TCWOSEIvCFIACqD0W2KZvNrjlsq8I2QwY6AfYhaz.3k0mI2_SUnG9H3.F7zMOtMa_blQ274zJMwFGFRDIHvMkacJB_OwuKHXorzrr3Fx_xThzBO2jY.amI.FSaXDbN.12_CYX_GzJ5SlNwmFyt6f_srj7DRA.fsKuciedjsfRsA54mRfaYrDLQs7v8FQ; g_state={"i_l":0,"i_ll":1761754551608,"i_b":"ZIlb5pk61iEXmouwu0zL1pdhQOY/ytpOKXucEisCCKI"}; _hjSession_1950941=eyJpZCI6ImVlOGQyYWVkLWI2NDAtNDBlNi1iMmUwLTkwMzQzOGMxZmZiNCIsImMiOjE3NjE3NTQ1NTIyMTEsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _rdt_uuid=1761589639145.76803583-c9b7-4db0-be67-f3aa7f2a5efe; analytics_session_id=1761754552448; __hstc=256179476.25b8762c6d7b33678b29531d55cc09a4.1761589640689.1761589640689.1761754554128.2; __hssrc=1; __hssc=256179476.1.1761754554128; analytics_session_id.last_access=1761754805914; intercom-id-pgpbhph6=9d85b37a-b7e5-415b-9232-59b3c19a06ea; _ga_Z8D4WL3D4P=GS2.1.s1761754552$o2$g1$t1761754806$j60$l0$h0; _rdt_em=:cd2f3b9085a54c9e957b17ea3ff0d3013caf0259084ad28d3e286190ac1aa11f,3aa8639871d91d4b7d08d85ac3f2625896cebf4a57be671197f435d3fbeb79c3,bdf3e541487fe05af6768547aeb77019016adeceba78da9387145a68b4547424,bdf3e541487fe05af6768547aeb77019016adeceba78da9387145a68b4547424; thm-aid=29ef4121-e713-4d07-b825-00be40a6a18c'
        }
        with allure.step(f'Вызов метода: {url}'):
            response = requests.request("POST", url, headers=headers, data=payload)

        with allure.step(f'Проверка статус кода: {url}'):
            assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}. ' \
                                                                 f'Статуса код равен {response.status_code} '
