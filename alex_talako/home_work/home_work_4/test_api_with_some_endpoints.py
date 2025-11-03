import requests
import json
import allure
import pytest

@allure.epic('API тесты')
@allure.feature('Endpoint Challenges')
@allure.title('Проверка статус кода')
@pytest.mark.parametrize("url, expected_status_code" , [
    ("https://tryhackme.com/challenges", 200),
    ("https://tryhackme.com/challenges", 102),
    ("https://tryhackme.com/challenges", 304),
    ("https://tryhackme.com/challenges", 404),
    ("https://tryhackme.com/challenges", 500),
])

def test_api_challenge(url, expected_status_code):
    with allure.step('Подготовка тестовых данных'):
        url = "https://tryhackme.com/challenges"

        payload = {}
        headers = {
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
          'priority': 'u=0, i',
          'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'none',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
          'Cookie': 'thm-aid=829d6382-071a-4b26-96a9-119a3adde5ab; _csrf=0zR34f04pQ7Q_oBK3sYKiB7i; _hjSessionUser_1950941=eyJpZCI6IjQzNDQ1ZDA2LThlOTctNTFhYi1hNGVkLTdiN2M4YTk3ZGQxMiIsImNyZWF0ZWQiOjE3NjE2Mzk5MTQ3MzMsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.676568251.1761639915; ajs_anonymous_id=829d6382-071a-4b26-96a9-119a3adde5ab; thm-amplitude-device-id=829d6382-071a-4b26-96a9-119a3adde5ab; hubspotutk=09436f71ef7d2d9e584add619e779fdf; __hssrc=1; intercom-device-id-pgpbhph6=cffa0771-47f2-4dee-923a-853674dda4d7; thm-amplitude-session-id=1761639915439; analytics_session_id=1761639915439; cookieconsent_status=dismiss; _shopify_y=b8b104ca-a7d3-4878-be15-24b61685ed89; connect.sid=s%3AIX4V_9egq85a9MkiX-S5Vpwz1QTs33tr.rt3%2B4q2wTpN6LBMNQ1hFZnxpWv4NIo6O%2BqVRNlx9oDE; cf_clearance=oMMGcfMnE1hNw4Y1oA2lj9nP7dsN37kB53k9eQU5l2w-1761646385-1.2.1.1-BHzrNudGoPR.1NNmv5JhS_HjF50QRztHdzHPEOvAATWRH9BBtKy1bUL3tExn_PSHQWF79e5EbqTufKPP7lP1kQG8Ym4FbNH_VzdcIzZgZfXRWdIVEntuz430J42BVYaotRjm6zLcjLbZdhrorSMJKnIaTApgj7Pb5nyM9kNtaDS_dUac2MDWhMoY6EIz2zG_I9jBjURxwQBaXUlete0t892LfSF6bjmzYLsTwjcnKOQ; g_state={"i_l":0,"i_ll":1762149523574,"i_b":"W/Cz6DZ+rw4//wMn9gak8kme5vhbVlPe3Ug70M0VHBI"}; _rdt_uuid=1761639914448.b464d89f-c604-4d4c-91dd-1fd571bc46db; __hstc=256179476.09436f71ef7d2d9e584add619e779fdf.1761639916034.1762094556296.1762149528011.25; gbStickyBuckets__anonymousId||829d6382-071a-4b26-96a9-119a3adde5ab={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%22829d6382-071a-4b26-96a9-119a3adde5ab%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22google-one-tap-auto-login__0%22:%221%22%2C%22new-homepage__0%22:%223%22%2C%22linkedin-social-login__0%22:%220%22}}; _hjSession_1950941=eyJpZCI6ImJlN2M0YjA4LWFmZjUtNDUxMC1hOGY2LTM3YjEyNTNjMTg1MiIsImMiOjE3NjIxNjEzMjA4NzYsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; analytics_session_id=1762161320897; _rdt_em=:e9aff251222f82b670e8d33ac5b56e59dbaa79bab3ee91d10af3f3b55a61ba6b,b8ec1d2a83e0501f53982c59e311b86c261d43df9300b729ed2ddca71681ac90; _gcl_au=1.1.2016557848.1761639913.764678889.1762161334.1762161451; logged-in-hint=687e46b8ad61437da3d8465f; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22talako00%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D; _cioid=687e46b8ad61437da3d8465f; ajs_user_id=687e46b8ad61437da3d8465f; gbStickyBuckets__id||687e46b8ad61437da3d8465f=%7B%22attributeName%22%3A%22id%22%2C%22attributeValue%22%3A%22687e46b8ad61437da3d8465f%22%2C%22assignments%22%3A%7B%22improvement-offensive-security-intro__0%22%3A%220%22%7D%7D; intercom-session-pgpbhph6=eEw5aHlSQ014L3JDRFB4RHpaRGRMZTZBK2VrSTlwc1B4ZHI4bGlaSmZyYmhQZ01iR3Z4UC95ZlE5UFZtL2ltQXZ3amp4bTRWYlp3cmIrZTlCd3NTYmROc1BxOWJRT0dQYVdzeHR4Z1o2MjA9LS1LUkR2REJXRFB1R1cvRTlEVnFveHpRPT0=--1c442b3bf6947c0285d52c9e81432897eeab8e15; _hjHasCachedUserAttributes=true; analytics_session_id.last_access=1762162114064; _ga_Z8D4WL3D4P=GS2.1.s1762161321$o32$g1$t1762162115$j55$l0$h0; logged-in-hint=687e46b8ad61437da3d8465f; thm-aid=829d6382-071a-4b26-96a9-119a3adde5ab; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22talako00%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D'
        }
        with allure.step(f'Вызов метода: {url}'):
            response = requests.request("GET", url, headers=headers, data=payload)

        with allure.step(f'Проверка статус кода для: {url}'):
            assert response.status_code == expected_status_code, f'Статус код равен {expected_status_code}, а должен быть равен {response.status_code}'



@allure.epic('API тесты')
@allure.feature('Endpoint Dashboard')
@allure.title('Проверка статус кода')
@pytest.mark.parametrize("url, expected_status_code" , [
    ("https://tryhackme.com/dashboard", 102),
    ("https://tryhackme.com/dashboard", 302),
    ("https://tryhackme.com/dashboard", 200),
    ("https://tryhackme.com/dashboard", 4000),
    ("https://tryhackme.com/dashboard", 999),
])

def test_api_dashboard(url, expected_status_code):
    with allure.step('Подготовка тестовых данных'):
        url = "https://tryhackme.com/dashboard"

        payload = {}
        headers = {
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
          'priority': 'u=0, i',
          'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'none',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
          'Cookie': 'thm-aid=829d6382-071a-4b26-96a9-119a3adde5ab; _csrf=0zR34f04pQ7Q_oBK3sYKiB7i; _hjSessionUser_1950941=eyJpZCI6IjQzNDQ1ZDA2LThlOTctNTFhYi1hNGVkLTdiN2M4YTk3ZGQxMiIsImNyZWF0ZWQiOjE3NjE2Mzk5MTQ3MzMsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.676568251.1761639915; ajs_anonymous_id=829d6382-071a-4b26-96a9-119a3adde5ab; thm-amplitude-device-id=829d6382-071a-4b26-96a9-119a3adde5ab; hubspotutk=09436f71ef7d2d9e584add619e779fdf; __hssrc=1; intercom-device-id-pgpbhph6=cffa0771-47f2-4dee-923a-853674dda4d7; thm-amplitude-session-id=1761639915439; analytics_session_id=1761639915439; cookieconsent_status=dismiss; _shopify_y=b8b104ca-a7d3-4878-be15-24b61685ed89; connect.sid=s%3AIX4V_9egq85a9MkiX-S5Vpwz1QTs33tr.rt3%2B4q2wTpN6LBMNQ1hFZnxpWv4NIo6O%2BqVRNlx9oDE; cf_clearance=oMMGcfMnE1hNw4Y1oA2lj9nP7dsN37kB53k9eQU5l2w-1761646385-1.2.1.1-BHzrNudGoPR.1NNmv5JhS_HjF50QRztHdzHPEOvAATWRH9BBtKy1bUL3tExn_PSHQWF79e5EbqTufKPP7lP1kQG8Ym4FbNH_VzdcIzZgZfXRWdIVEntuz430J42BVYaotRjm6zLcjLbZdhrorSMJKnIaTApgj7Pb5nyM9kNtaDS_dUac2MDWhMoY6EIz2zG_I9jBjURxwQBaXUlete0t892LfSF6bjmzYLsTwjcnKOQ; g_state={"i_l":0,"i_ll":1762149523574,"i_b":"W/Cz6DZ+rw4//wMn9gak8kme5vhbVlPe3Ug70M0VHBI"}; _rdt_uuid=1761639914448.b464d89f-c604-4d4c-91dd-1fd571bc46db; __hstc=256179476.09436f71ef7d2d9e584add619e779fdf.1761639916034.1762094556296.1762149528011.25; gbStickyBuckets__anonymousId||829d6382-071a-4b26-96a9-119a3adde5ab={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%22829d6382-071a-4b26-96a9-119a3adde5ab%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22google-one-tap-auto-login__0%22:%221%22%2C%22new-homepage__0%22:%223%22%2C%22linkedin-social-login__0%22:%220%22}}; _hjSession_1950941=eyJpZCI6ImJlN2M0YjA4LWFmZjUtNDUxMC1hOGY2LTM3YjEyNTNjMTg1MiIsImMiOjE3NjIxNjEzMjA4NzYsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; analytics_session_id=1762161320897; _rdt_em=:e9aff251222f82b670e8d33ac5b56e59dbaa79bab3ee91d10af3f3b55a61ba6b,b8ec1d2a83e0501f53982c59e311b86c261d43df9300b729ed2ddca71681ac90; _gcl_au=1.1.2016557848.1761639913.764678889.1762161334.1762161451; logged-in-hint=687e46b8ad61437da3d8465f; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22talako00%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D; _cioid=687e46b8ad61437da3d8465f; ajs_user_id=687e46b8ad61437da3d8465f; gbStickyBuckets__id||687e46b8ad61437da3d8465f=%7B%22attributeName%22%3A%22id%22%2C%22attributeValue%22%3A%22687e46b8ad61437da3d8465f%22%2C%22assignments%22%3A%7B%22improvement-offensive-security-intro__0%22%3A%220%22%7D%7D; intercom-session-pgpbhph6=eEw5aHlSQ014L3JDRFB4RHpaRGRMZTZBK2VrSTlwc1B4ZHI4bGlaSmZyYmhQZ01iR3Z4UC95ZlE5UFZtL2ltQXZ3amp4bTRWYlp3cmIrZTlCd3NTYmROc1BxOWJRT0dQYVdzeHR4Z1o2MjA9LS1LUkR2REJXRFB1R1cvRTlEVnFveHpRPT0=--1c442b3bf6947c0285d52c9e81432897eeab8e15; _hjHasCachedUserAttributes=true; analytics_session_id.last_access=1762162114064; _ga_Z8D4WL3D4P=GS2.1.s1762161321$o32$g1$t1762162115$j55$l0$h0; logged-in-hint=687e46b8ad61437da3d8465f; thm-aid=829d6382-071a-4b26-96a9-119a3adde5ab; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22talako00%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D'
        }

        with allure.step(f'Вызов метода: {url}'):
            response = requests.request("GET", url, headers=headers, data=payload)

        with allure.step(f'Проверка статус кода для: {url}'):
            assert response.status_code == expected_status_code, f'Статус код равен {expected_status_code}, а должен быть равен {response.status_code}'



@allure.epic('API тесты')
@allure.feature('Endpoint Hacktivities')
@allure.title('Проверка статус кода')
@pytest.mark.parametrize("url, expected_status_code" , [
    ("https://tryhackme.com/hacktivities", 102),
    ("https://tryhackme.com/hacktivities", 302),
    ("https://tryhackme.com/hacktivities", 502),
    ("https://tryhackme.com/hacktivities", 202),
    ("https://tryhackme.com/hacktivities", 200),
])

def test_api_hacktivities(url, expected_status_code):
    with allure.step('Подготовка тестовых данных'):
        url = "https://tryhackme.com/hacktivities"

        payload = {}
        headers = {
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
          'priority': 'u=0, i',
          'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'none',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
          'Cookie': 'thm-aid=829d6382-071a-4b26-96a9-119a3adde5ab; _csrf=0zR34f04pQ7Q_oBK3sYKiB7i; _hjSessionUser_1950941=eyJpZCI6IjQzNDQ1ZDA2LThlOTctNTFhYi1hNGVkLTdiN2M4YTk3ZGQxMiIsImNyZWF0ZWQiOjE3NjE2Mzk5MTQ3MzMsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.676568251.1761639915; ajs_anonymous_id=829d6382-071a-4b26-96a9-119a3adde5ab; thm-amplitude-device-id=829d6382-071a-4b26-96a9-119a3adde5ab; hubspotutk=09436f71ef7d2d9e584add619e779fdf; __hssrc=1; intercom-device-id-pgpbhph6=cffa0771-47f2-4dee-923a-853674dda4d7; thm-amplitude-session-id=1761639915439; analytics_session_id=1761639915439; cookieconsent_status=dismiss; _shopify_y=b8b104ca-a7d3-4878-be15-24b61685ed89; connect.sid=s%3AIX4V_9egq85a9MkiX-S5Vpwz1QTs33tr.rt3%2B4q2wTpN6LBMNQ1hFZnxpWv4NIo6O%2BqVRNlx9oDE; cf_clearance=oMMGcfMnE1hNw4Y1oA2lj9nP7dsN37kB53k9eQU5l2w-1761646385-1.2.1.1-BHzrNudGoPR.1NNmv5JhS_HjF50QRztHdzHPEOvAATWRH9BBtKy1bUL3tExn_PSHQWF79e5EbqTufKPP7lP1kQG8Ym4FbNH_VzdcIzZgZfXRWdIVEntuz430J42BVYaotRjm6zLcjLbZdhrorSMJKnIaTApgj7Pb5nyM9kNtaDS_dUac2MDWhMoY6EIz2zG_I9jBjURxwQBaXUlete0t892LfSF6bjmzYLsTwjcnKOQ; g_state={"i_l":0,"i_ll":1762149523574,"i_b":"W/Cz6DZ+rw4//wMn9gak8kme5vhbVlPe3Ug70M0VHBI"}; _rdt_uuid=1761639914448.b464d89f-c604-4d4c-91dd-1fd571bc46db; __hstc=256179476.09436f71ef7d2d9e584add619e779fdf.1761639916034.1762094556296.1762149528011.25; gbStickyBuckets__anonymousId||829d6382-071a-4b26-96a9-119a3adde5ab={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%22829d6382-071a-4b26-96a9-119a3adde5ab%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22google-one-tap-auto-login__0%22:%221%22%2C%22new-homepage__0%22:%223%22%2C%22linkedin-social-login__0%22:%220%22}}; _hjSession_1950941=eyJpZCI6ImJlN2M0YjA4LWFmZjUtNDUxMC1hOGY2LTM3YjEyNTNjMTg1MiIsImMiOjE3NjIxNjEzMjA4NzYsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; analytics_session_id=1762161320897; _rdt_em=:e9aff251222f82b670e8d33ac5b56e59dbaa79bab3ee91d10af3f3b55a61ba6b,b8ec1d2a83e0501f53982c59e311b86c261d43df9300b729ed2ddca71681ac90; _gcl_au=1.1.2016557848.1761639913.764678889.1762161334.1762161451; logged-in-hint=687e46b8ad61437da3d8465f; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22talako00%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D; _cioid=687e46b8ad61437da3d8465f; ajs_user_id=687e46b8ad61437da3d8465f; gbStickyBuckets__id||687e46b8ad61437da3d8465f=%7B%22attributeName%22%3A%22id%22%2C%22attributeValue%22%3A%22687e46b8ad61437da3d8465f%22%2C%22assignments%22%3A%7B%22improvement-offensive-security-intro__0%22%3A%220%22%7D%7D; intercom-session-pgpbhph6=eEw5aHlSQ014L3JDRFB4RHpaRGRMZTZBK2VrSTlwc1B4ZHI4bGlaSmZyYmhQZ01iR3Z4UC95ZlE5UFZtL2ltQXZ3amp4bTRWYlp3cmIrZTlCd3NTYmROc1BxOWJRT0dQYVdzeHR4Z1o2MjA9LS1LUkR2REJXRFB1R1cvRTlEVnFveHpRPT0=--1c442b3bf6947c0285d52c9e81432897eeab8e15; _hjHasCachedUserAttributes=true; analytics_session_id.last_access=1762162114064; _ga_Z8D4WL3D4P=GS2.1.s1762161321$o32$g1$t1762162115$j55$l0$h0; logged-in-hint=687e46b8ad61437da3d8465f; thm-aid=829d6382-071a-4b26-96a9-119a3adde5ab; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22talako00%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D'
        }

        with allure.step(f'Вызов метода: {url}'):
            response = requests.request("GET", url, headers=headers, data=payload)

        with allure.step(f'Проверка статус кода для: {url}'):
            assert response.status_code == expected_status_code, f'Статус код равен {expected_status_code}, а должен быть равен {response.status_code}'



