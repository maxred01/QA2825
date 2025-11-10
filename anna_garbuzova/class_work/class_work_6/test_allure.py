import requests, allure

@allure.epic("API Tests")
@allure.feature("Форма обратной связи")
@allure.story("Позитивные тесты")
@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for authentication")

def test_api_post():
    with allure.step('Подготовка тестовых данных'):
        url = "https://zelgavan.by/forms/callback"

        payload = {'name': 'test',
                   'phone': '+375 (00) 000-00-00',
                   'form_name': 'Форма расскажем больше'}
        files = [

        ]
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'origin': 'https://zelgavan.by',
            'priority': 'u=1, i',
            'referer': 'https://zelgavan.by/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36',
            'x-csrf-token': 'k6mZnjAUYJNtfBW8DxrrOSMpeafSYCh5aiaMY008',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'roistat_visit=2881243; roistat_first_visit=2881243; roistat_visit_cookie_expire=1209600; roistat_is_need_listen_requests=0; roistat_is_save_data_in_cookie=1; roistat_marker=google4_g_180943209589_759618475365_%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%B0%D1%8F%20%D0%B3%D0%B0%D0%B2%D0%B0%D0%BD%D1%8C; roistat_marker_old=google4_g_180943209589_759618475365_%D0%B7%D0%B5%D0%BB%D0%B5%D0%BD%D0%B0%D1%8F%20%D0%B3%D0%B0%D0%B2%D0%B0%D0%BD%D1%8C; roistat_gclid=Cj0KCQjwsPzHBhDCARIsALlWNG2Pz6awsZbBVswripBUEMGWj3YpJO8lgViMSDkUooJG7L4Th9ozS94aAo6NEALw_wcB; _gcl_gs=2.1.k1$i1761589515$u186048162; _ga=GA1.1.172067973.1761589519; _gcl_au=1.1.1759978084.1761589519; _ym_uid=1761589519654701270; _ym_d=1761589519; _fbp=fb.1.1761589519440.732130255842181496; ___dc=b8f93ee4-207a-41e4-9eb7-2ae3bdf4fb2f; ACCEPT_COOKIES=1; ACCEPT_COOKIES_FUNC=1; ACCEPT_COOKIES_ANALIT=1; _tt_enable_cookie=1; _ttp=01K8KENWFKFDC5WW6QXFSHFP0Z_.tt.1; _gcl_aw=GCL.1761589766.Cj0KCQjwsPzHBhDCARIsALlWNG2Pz6awsZbBVswripBUEMGWj3YpJO8lgViMSDkUooJG7L4Th9ozS94aAo6NEALw_wcB; roistat_call_tracking=1; roistat_emailtracking_email=null; roistat_emailtracking_tracking_email=null; roistat_emailtracking_emails=null; zelgavan_ct_ref_c=https://zelgavan.by/; zelgavan_ct_id=33584884; zelgavan_ct_ref_l=https://zelgavan.by/; zelgavan_ct_ga=1; zelgavan_ct_ya=1; zelgavan_ct_roi=1; zelgavan_ct_fb=1; zelgavan_ct_ga4_session=1; _ym_isad=2; XSRF-TOKEN=eyJpdiI6Ilp6RVhtNTlJMTBBYkd2cXVtMmdmdnc9PSIsInZhbHVlIjoia1dHcVZibmVDbG9EV1crQjd0RUNvREtka3JUTkYzWldOVzNpM3VkVjRXM25MTVJ0ZDdWQVJYS3ZUMzhJejFzR0VJWU54NXBaSkFpUVZZOGxlYlRuQzNKNkhyeDVwUHUyOGNxVDgxZWpIL3V0TC9CQW1QWmtldE95UWV1L3hyWjgiLCJtYWMiOiI5NTk4MjhiMTZhMDMxNmJiNGU3OTRkNjg5NDA5MmY2YzBiY2M2ODI3NzIzZTFlNzhhODE5YjdhOWY5NGZhMzQ0IiwidGFnIjoiIn0%3D; zelgavan_session=eyJpdiI6IjhUakMranRrR2c0d29aLzVnY0VJWUE9PSIsInZhbHVlIjoiZ0dtdGFtMVdKK0hTTWRndWRUMmhuN3NPMU1memdwMFNTaG5PaEhaWGw5OGZDMUtWOXF2bTZOVUNwTEY1aFlod3ZrUG9nY1VTMjdIN1hzdHQ1aWtVZSswbmUzZXVsbFdVdWE5VEZtK3NnR2JCeDdKVVFoQ2VZRjA1Zmtka0F6V1giLCJtYWMiOiIzMDA3MzA3MmY2ODMwMGU3YWRkODczN2ZkNWFhYWExNzA3YmFmNzVhYzI0MDgzYmFhYTU2MmRlOWZjZjY3YmY4IiwidGFnIjoiIn0%3D; cookie=eyJpdiI6InRJc0Q3QVV2ZWRtdURaUHJta25Xcnc9PSIsInZhbHVlIjoiZjZCTjV1UXJoWFRrUmxtRTJ4Q2pTdUE0ako3YlhyYi81cjdWQmJkdjROTyt3RDlGeXgxSTA0VUJVL3VadGVsYSIsIm1hYyI6ImFlZTkwZWUyM2UwOWM0YWYxYjYzMjhlYmY4ZjlkYWY1YTc4MzFiYWMwYWRmYmI2MmRmYjAwOGI1ZDZlMzMwYzMiLCJ0YWciOiIifQ%3D%3D; _ym_visorc=w; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails; invitation=1; zelgavan_ct_s=eyJwaG9uZXMiOnsiKzM3NTI5MzAwMDAwMCI6IiszNzU0NDU5MTIzNjkiLCIrMzc1MjkzODA3MDkwIjoiKzM3NTQ0NTkxMjM2OSJ9LCJyZWdleHAiOiIiLCJleHAiOiIyMDI1LTEwLTI5VDE2OjI3OjEwLjI1NloifQ==; _ga_CVJQ1803QP=GS2.1.s1761754581$o4$g1$t1761754944$j30$l0$h1404243276; ttcsid=1761754582545::nbnoH8W3tBKmTQ2se8Mi.4.1761754974013.0; ttcsid_CPK212RC77U6NIAFNGOG=1761754582545::p6EThbX0cQ0HQiW_tHir.4.1761754974014.0; XSRF-TOKEN=eyJpdiI6Im1HOU11MXRkQTR0TGkrOExZNHArcUE9PSIsInZhbHVlIjoidFZtaWM1ZVNjV0lYWUtQakU2cThPUTQ3SlF0WWlzYi9aczRXWFlxUm1QeUN3VDk1UGs2bUtxbTZyQ1VtSWN3d01sUlkvU3R5a3ljSmJCUVNnazdLTVJPVTIyZUIybWlWUnQvejVydXhHanBDYVNBQkxVeWJVUXRWUlRDSDkrdDMiLCJtYWMiOiI4MTM3MzliNzY5YjhmODE0NDQzNWQ4YmY2ZDhjMmY2NDg4NGJhMDlhM2M3Mzc2MDU2Y2JiZGRjZDI2OGIyY2IyIiwidGFnIjoiIn0%3D; cookie=eyJpdiI6InhoZ0FJYlJJSWJwUWJKakIxS3Qwc2c9PSIsInZhbHVlIjoiRlQ4Yk9IeFdlekl6Y1N5S2F0d2tVNUFrdlVMdC95VG1wUWhLRE5rbTVoRENYd0dFSWJnbEFzWnp0a0VMb2YrTyIsIm1hYyI6IjNhOWY4Njc3ZjhiZDM3ZDEyYzQ3NWMxZGNjYTAwNDAwYTQ0YTE5OTNiM2EzZGFhN2RjY2Y1NzA5NWNlY2M3OGEiLCJ0YWciOiIifQ%3D%3D; roistat_call_tracking=1; roistat_emailtracking_email=null; roistat_emailtracking_emails=null; roistat_emailtracking_tracking_email=null; zelgavan_session=eyJpdiI6Im5rSUFHOTdsbG9WZ1Z1OWJzOEx0RUE9PSIsInZhbHVlIjoiSXlKeGpyN3BIcmVSUCt3Vm1BMzF6cGhQb3FHcnFSc0xsUCt1cUdTSnZBcEt5QktHbW5xTmpZYnVLSjBHOUp1RHAwVWRSWklqTEpMZFRyaDhKQWpNREhHZXNYTXl5ODdraHB2SjA2MGYwZzRvdDFPTXVKMXVpQVZTWTVwdDdxMTMiLCJtYWMiOiI0ZjNhMjUxM2JkN2Y3MWE2NDU4ZGIyYzk0NzJiZWE4OTgwNjlmNGRjNmQ3OTk3NDBhYmE1OTBlZTgzOGI0MzdkIiwidGFnIjoiIn0%3D'
        }

    with allure.step('Вызов метода forms/callback'):
        response = requests.request("POST", url, headers=headers, data=payload, files=files)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200,f'Status code is {response.status_code}'


