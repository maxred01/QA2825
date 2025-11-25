import pytest
import requests
import json
import allure
url = "https://tryhackme.com/"

@allure.title('Апи тесты')
@allure.story(f'Проверки статус кода всех ссылок на сайте: {url}')
@pytest.mark.parametrize("status_code, url, label", [
    (200, "https://store.tryhackme.com/", "Swag Shop"),
    (200, "https://discord.com/invite/tryhackme", ""),
    (200, "https://www.facebook.com/people/Tryhackme/100069557747714/", ""),
    (200, "https://tryhackme.com/", ""),
    (200, "https://careers.tryhackme.com/", "Work at TryHackMe"),
    (200, "https://tryhackme.com/hacktivities", "Learn"),
    (200, "https://tryhackme.com/contact", "Contact Us"),
    (200, "https://tryhackme.com/subscriptions", "Buy Vouchers"),
    (200, "https://tryhackme.com/path/outline/azuresecurity", "Defending AzureEnrol"),
    (200, "https://tryhackme.com/legal/acceptable-use-policy", "Acceptable Use Polic"),
    (200, "https://tryhackme.com/path/outline/web", "Web FundamentalsEnro"),
    (200, "https://tryhackme.com/business", "Business"),
    (200, "https://tryhackme.com/certification/security-analyst-level-1", "Defensive Certificat"),
    (200, "https://tryhackme.com/path/outline/devsecops", "DevSecOpsEnroll in P"),
    (200, "https://tryhackme.com/path/outline/pentestplus", "CompTIA Pentest+Enro"),
    (200, "https://tryhackme.com/games/koth", "Competitive Hacking"),
    (200, "https://tryhackme.com/path/outline/advancedendpointinvestigations", "Advanced Endpoint In"),
    (200, "https://tryhackme.com/about", "About Us"),
    (200, "https://tryhackme.com/legal/privacy-policy", "Privacy Policy"),
    (200, "https://tryhackme.com/resources/blog", "Blog"),
    (200, "https://tryhackme.com/pricing", "Pricing"),
    (200, "https://tryhackme.com/glossary", "Glossary"),
    (200, "https://www.youtube.com/channel/UCRnWD3BsY5Co2MMETB7lHQw", ""),
    (200, "https://tryhackme.com/classrooms", "Learn More"),
    (200, "https://tryhackme.com/path/outline/pentesting", "Offensive Pentesting"),
    (200, "https://tryhackme.com/legal/terms-of-use", "Terms of Use"),
    (200, "https://tryhackme.com/path/outline/redteaming", "Red TeamingEnroll in"),
    (200, "https://tryhackme.com/path/outline/cybersecurity101", "Cyber Security 101En"),
    (200, "https://tryhackme.com/path/outline/attackinganddefendingaws", "Attacking and Defend"),
    (200, "https://tryhackme.com/path/outline/soclevel1", "SOC Level 1Enroll in"),
    (200, "https://tryhackme.com/legal/ai-terms-of-use", "AI Terms of Use"),
    (200, "https://tryhackme.com/careers", "Careers in Cyber"),
    (200, "https://tryhackme.com/legal/cookie-policy", "Cookie Policy"),
    (200, "https://tryhackme.com/path/outline/presecurity", "Pre SecurityEnroll i"),
    (200, "https://tryhackme.com/resources/newsroom", "Newsroom"),
    (200, "https://tryhackme.com/path/outline/soclevel2", "SOC Level 2Enroll in"),
    (200, "https://tryhackme.com/path/outline/security-engineer-training", "Security EngineerEnr"),
    (200, "https://tryhackme.com/path/outline/jrpenetrationtester", "Jr Penetration Teste"),
    (200, "https://tryhackme.com/path/outline/webapppentesting", "Web Application Pent"),
    (200, "https://tryhackme.com/signup", "Join for FREE"),
    (200, "https://tryhackme.com/hacktivities", "Learn"),
    (200, "https://tryhackme.com/", ""),
    (200, "https://tryhackme.com/pricing", "Pricing"),
    (200, "https://tryhackme.com/business", "Business"),
    (200, "https://tryhackme.com/legal/terms-of-use", "Read more"),
    (200, "https://tryhackme.com/classrooms", "For Education"),
    (200, "https://tryhackme.com/hacktivities", "Hands-on labs"),
    (200, "https://tryhackme.com/business", "For Business"),
    (999, "https://www.linkedin.com/company/tryhackme/", "999"),
    (300, "https://twitter.com/tryhackme", ""),
    (300, "https://instagram.com/realtryhackme", ""),
    (300, "https://tryhackme.com/forum", "Forum"),
    (300, "https://www.pinterest.co.uk/RealTryHackMe/", ""),
    (300, "https://business.tryhackme.com/", "Learn More"),

])

def test_links_api_get(status_code, url, label):
    with allure.step(f'Подготовка тестовых данных {label}'):
        url = "https://tryhackme.com/"

        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'Cookie': 'thm-aid=29ef4121-e713-4d07-b825-00be40a6a18c; _csrf=6Z9P-3gMNsfO1tjA3wMaA7Rc; cf_clearance=5goZ7f0NS3C7Eg.kEwO7CKSWwB.zBSkj20iLYiQZwuw-1761589638-1.2.1.1-rbLL7glvTMNxF1Sz5oqDOEJaXQ3_HDJLSurrk7eCpvrO.08auHftR0sjniuJqLDxmeoAjSHLoudD2GiJDSrFz6sXoSwXsUfO6GwF10nH6tAkWCwbbsyYIcieuEnOc8S3._VIoq1GaaSg7CHaVtfbEQ6JmadSWl6hrvm7vA5u7Iih.5770tiKmkr7rZ7JGmzfn51cwDILlG7IS14wHk46rEGnO3ecO7OFcBkmYg_Ys5M; _gcl_au=1.1.1404139791.1761589639; _hjSessionUser_1950941=eyJpZCI6IjliOTMyYzQxLTE4ODctNTc3My04ZjJjLWMzNWRjN2E2NGM2YiIsImNyZWF0ZWQiOjE3NjE1ODk2Mzg3NzUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1950941=eyJpZCI6ImI4YTBmYTU5LWE4MTAtNDZjNy05ODY5LTQ5OTU1MGE1OWUwMCIsImMiOjE3NjE1ODk2Mzg3NzYsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; gbStickyBuckets__anonymousId||29ef4121-e713-4d07-b825-00be40a6a18c={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%2229ef4121-e713-4d07-b825-00be40a6a18c%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22google-one-tap-auto-login__0%22:%221%22}}; g_state={"i_l":0,"i_ll":1761589638929,"i_b":"pemL+Tr7sqRu/ICqBv8avJ5Hn1pGeDfhMPeTjee0HLM"}; ajs_anonymous_id=29ef4121-e713-4d07-b825-00be40a6a18c; _ga=GA1.1.1058267343.1761589639; _rdt_uuid=1761589639145.76803583-c9b7-4db0-be67-f3aa7f2a5efe; _fbp=fb.1.1761589639155.592488567316109178; thm-amplitude-device-id=29ef4121-e713-4d07-b825-00be40a6a18c; analytics_session_id=1761589639345; __hstc=256179476.25b8762c6d7b33678b29531d55cc09a4.1761589640689.1761589640689.1761589640689.1; hubspotutk=25b8762c6d7b33678b29531d55cc09a4; __hssrc=1; __hssc=256179476.1.1761589640689; intercom-device-id-pgpbhph6=1ace7cda-b13c-47ef-a660-662960313f90; analytics_session_id.last_access=1761589773805; intercom-id-pgpbhph6=36f27b42-c0f6-4b7a-937a-fa33d6856387; _ga_Z8D4WL3D4P=GS2.1.s1761589639$o1$g1$t1761589774$j49$l0$h0; thm-aid=29ef4121-e713-4d07-b825-00be40a6a18c'
        }
        with allure.step(f'Вызов метода: {url}'):
            response = requests.request("GET", url, headers=headers, data=payload)
        with allure.step(f'Проверка статус кода ссылок на сайте: {url}'):
            assert response.status_code == status_code, f'Статус код не равен {status_code}. Статус код должен быть равен {response.status_code}'



@allure.title('Апи тесты другого формата')
@allure.story(f'Проверки статус кода сайта: {url}')
@pytest.mark.parametrize("url, expected_status_code", [
    ("https://tryhackme.com/", 200),
    ("https://tryhackme.com/", 300),
    ("https://tryhackme.com/", 102),
    ("https://tryhackme.com/", 404),
])

def test_api_get_2(url, expected_status_code):
    with allure.step('Подготовка тестовых данных'):
        url = "https://tryhackme.com/"

        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
            'Cookie': 'thm-aid=29ef4121-e713-4d07-b825-00be40a6a18c; _csrf=6Z9P-3gMNsfO1tjA3wMaA7Rc; cf_clearance=5goZ7f0NS3C7Eg.kEwO7CKSWwB.zBSkj20iLYiQZwuw-1761589638-1.2.1.1-rbLL7glvTMNxF1Sz5oqDOEJaXQ3_HDJLSurrk7eCpvrO.08auHftR0sjniuJqLDxmeoAjSHLoudD2GiJDSrFz6sXoSwXsUfO6GwF10nH6tAkWCwbbsyYIcieuEnOc8S3._VIoq1GaaSg7CHaVtfbEQ6JmadSWl6hrvm7vA5u7Iih.5770tiKmkr7rZ7JGmzfn51cwDILlG7IS14wHk46rEGnO3ecO7OFcBkmYg_Ys5M; _gcl_au=1.1.1404139791.1761589639; _hjSessionUser_1950941=eyJpZCI6IjliOTMyYzQxLTE4ODctNTc3My04ZjJjLWMzNWRjN2E2NGM2YiIsImNyZWF0ZWQiOjE3NjE1ODk2Mzg3NzUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1950941=eyJpZCI6ImI4YTBmYTU5LWE4MTAtNDZjNy05ODY5LTQ5OTU1MGE1OWUwMCIsImMiOjE3NjE1ODk2Mzg3NzYsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; gbStickyBuckets__anonymousId||29ef4121-e713-4d07-b825-00be40a6a18c={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%2229ef4121-e713-4d07-b825-00be40a6a18c%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22google-one-tap-auto-login__0%22:%221%22}}; g_state={"i_l":0,"i_ll":1761589638929,"i_b":"pemL+Tr7sqRu/ICqBv8avJ5Hn1pGeDfhMPeTjee0HLM"}; ajs_anonymous_id=29ef4121-e713-4d07-b825-00be40a6a18c; _ga=GA1.1.1058267343.1761589639; _rdt_uuid=1761589639145.76803583-c9b7-4db0-be67-f3aa7f2a5efe; _fbp=fb.1.1761589639155.592488567316109178; thm-amplitude-device-id=29ef4121-e713-4d07-b825-00be40a6a18c; analytics_session_id=1761589639345; __hstc=256179476.25b8762c6d7b33678b29531d55cc09a4.1761589640689.1761589640689.1761589640689.1; hubspotutk=25b8762c6d7b33678b29531d55cc09a4; __hssrc=1; __hssc=256179476.1.1761589640689; intercom-device-id-pgpbhph6=1ace7cda-b13c-47ef-a660-662960313f90; analytics_session_id.last_access=1761589773805; intercom-id-pgpbhph6=36f27b42-c0f6-4b7a-937a-fa33d6856387; _ga_Z8D4WL3D4P=GS2.1.s1761589639$o1$g1$t1761589774$j49$l0$h0; thm-aid=29ef4121-e713-4d07-b825-00be40a6a18c'
        }
        with allure.step(f'Вызов метода: {url}'):
            response = requests.request("GET", url, headers=headers, data=payload)
        with allure.step(f'Проверка статус кода: {url}'):
            assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}. Статус код должен быть равен {response.status_code}'