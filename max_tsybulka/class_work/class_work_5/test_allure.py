import pytest, json, requests, random, allure


@allure.epic("API тесты")
@allure.feature("Авторизация")
@allure.story("Позитивные тесты")
@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for authentication")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://tryhackme.com/", name="Website")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
def test_api_post():
    """Этот тест делает что и мы чисто хотим понять че делает title"""
    with allure.step('Подготовка тестовых данных для api'):
        url = "https://tryhackme.com/api/v2/auth/login"

        payload = json.dumps({
            "email": 'test@gnail.com',
            "password": '12345qwer',
        })

        headers = {
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'baggage': 'sentry-environment=production,sentry-release=production-341f73a2f0,sentry-public_key=175180b5f191796714d2f9138c06c76a,sentry-trace_id=0788622e23204baeb09db99b35bdd374',
            'content-type': 'application/json',
            'csrf-token': 'UBw5n4vL-vNSsr0dI8vp_HznWeAaXYVL_F4M',
            'origin': 'https://tryhackme.com',
            'priority': 'u=1, i',
            'referer': 'https://tryhackme.com/login',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sentry-trace': '0788622e23204baeb09db99b35bdd374-847598fae659d9f5',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'x-recaptcha-response': '0cAFcWeA658QGL7I2Ny_v9lN9lB-q2HGmRog53md2ymOHbdbsGn1t9eT4wmyJkjM_7msKOHxBToY2xj3yWv7L_qw1s8ykU1v8CiFdU3Xh1U15LfLCNmKsts-n69X8fVRwJBnayDlDK98X_8W237LoWbVavbnbgikoryY670HSAmdNvU86lY2f2CtLrO_OoaEzlCPLP9NRpPgfj78bJrWZRXJ54DubFpaJNoomGB8duAy9dkF6qGP8NzNN7Yg10fLmgS4Y_iKAwAxblKuoE8d1oWEb0hIN9BAOoVH-tP06xbNeyqyEJ1iG4jx6aHs150Bh0hJxdUmdH9ny9XQZHy24yN6x4bm-XNZIGsSCVCn77Dbxl9vnzeJri1mrwz8u2GVgR3btqk4Pxy2pAtXA-PftvZAf99Cmw777SOc3kr_Tn5jhFBStnVf6qyyGko-FEwGVAuuwZ9z9hkNCCDAePVg6EoyR4QClkKL8bkB87yV-o6geeY4Lnvl3kcMsm0U6_TynuXE_2fdR3EeWlJ4TyWKIiU5jw5dY7ofhzXRRIxJBgcOMx-3twz3BAvW6mvTKDGEvDyu5nAfwUmUxzhk8mpdY4Q9x4kiv0t4mYs7Hf2n6kRtvCQLOnDNGWZfqCVNVE0amuOSm-0PfHesUstOahZuJmz2BApNnQZWwfbA-93n1-k14FOgGcmrpkEx7Pqb6_HFZjckrfOb9rVVUK5bE2-c8kOHp5YhjwZuJC5RScPa5WeZqaf0nnKYjFDtU',
            'Cookie': 'thm-aid=5ca3a18f-af35-4f8a-8123-216d77ff3fe7; _csrf=kWUfihfzU-25ghYeohvHHSwF; cf_clearance=1AiS5DFb5k4VxiIItttaeFpzj86uhkZh1h7o4yyq7jk-1761754570-1.2.1.1-X_OJatNV6tuzkXFab0U2Wr_jFM2ve1M2iBOFCbL0pj1PkKkZCxn5BLcnyT4vm6a4D5JUIwETleztHIOcbdqCqCjSZ1ILvNahEPgZa6Vu.L8yA8pSKLIlGGMt8PORPybQgpUhp9mtlO1.SO0BB.doBDPFvUrUdBIeo_fAZOEPOwAIlC9ec_7IdKUQXf1k1cmz_k6CjYoD3PbECbrGi0pyJmtTEuwxRQ2QlWqDyJygS24; gbStickyBuckets__anonymousId||5ca3a18f-af35-4f8a-8123-216d77ff3fe7={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%225ca3a18f-af35-4f8a-8123-216d77ff3fe7%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22new-homepage__0%22:%221%22%2C%22google-one-tap-auto-login__0%22:%221%22}}; g_state={"i_l":0,"i_ll":1761754570994,"i_b":"8HQlbnf5meDp4ukBCuYEhhPxPo5bLpa07HTTA24V+iM"}; ajs_anonymous_id=5ca3a18f-af35-4f8a-8123-216d77ff3fe7; _hjSessionUser_1950941=eyJpZCI6IjNlYzVkNDY1LWMxYzItNWU5Yy04MGZmLWE1NjQ2ZDk3NTU2ZiIsImNyZWF0ZWQiOjE3NjE3NTQ1NzE1OTcsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1950941=eyJpZCI6IjVkOGM3NjgyLTgwYjctNDUwMC1iOGM0LThmMmI2NDk4N2JhNyIsImMiOjE3NjE3NTQ1NzE1OTgsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1761754571692.15871996064966787; _ga=GA1.1.1814222461.1761754572; _rdt_uuid=1761754571927.49f110bd-424c-4965-96dc-1ae36749e13b; thm-amplitude-device-id=5ca3a18f-af35-4f8a-8123-216d77ff3fe7; analytics_session_id=1761754572134; __hstc=256179476.559368f46a62b34cf70d95b13fba0957.1761754573822.1761754573822.1761754573822.1; hubspotutk=559368f46a62b34cf70d95b13fba0957; __hssrc=1; __hssc=256179476.1.1761754573822; cookieconsent_status=dismiss; intercom-device-id-pgpbhph6=21c9fafd-d38f-40e1-bf09-98f5319c914e; analytics_session_id.last_access=1761754800769; intercom-id-pgpbhph6=839e00d0-9b75-4b16-9cce-4cda0dbc7d77; _ga_Z8D4WL3D4P=GS2.1.s1761754571$o1$g1$t1761754801$j60$l0$h0; _gcl_au=1.1.150541470.1761754571.1563137947.1761754866.1761754865; _rdt_em=:cd2f3b9085a54c9e957b17ea3ff0d3013caf0259084ad28d3e286190ac1aa11f,de5f8077e9a47cdd4a6df2c315473f0cd86106c838d69ad3371fd77f4c63f9da,bdf3e541487fe05af6768547aeb77019016adeceba78da9387145a68b4547424,bdf3e541487fe05af6768547aeb77019016adeceba78da9387145a68b4547424'
        }

    with allure.step(f'Вызов метода /api/v2/auth/login'):
        response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 401, f'Статус код не равен 200. Статус код равен {response.status_code}'
