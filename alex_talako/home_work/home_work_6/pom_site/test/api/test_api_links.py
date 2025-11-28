import pytest
import requests
import json
import allure


@allure.title('Апи тесты')
@allure.story(f'Проверка статус кодов всех ссылок на сайте TryHackMe и внешних ресурсов')
@pytest.mark.parametrize("expected_status_code, link_url, label", [
    (200, "https://store.tryhackme.com/", "Swag Shop"),
    (200, "https://discord.com/invite/tryhackme", ""),
    (400, "https://www.facebook.com/people/Tryhackme/100069557747714/", ""),
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
    (200, "https://www.linkedin.com/company/tryhackme/", "999"),
    (301, "https://twitter.com/tryhackme", ""),
    (301, "https://instagram.com/realtryhackme", ""),
    (301, "https://tryhackme.com/forum", "Forum"),
    (308, "https://www.pinterest.co.uk/RealTryHackMe/", ""),
    (302, "https://business.tryhackme.com/", "Learn More"),

])

def test_links_api_get(expected_status_code, link_url, label):
    with allure.step(f'Подготовка тестовых данных {label}'):
        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        }
        with allure.step(f'Вызов метода GET: {link_url}'):
            follow_redirects = expected_status_code == 200
            response = requests.request("GET", link_url, headers=headers, data=payload, allow_redirects=follow_redirects)
        with allure.step(f'Проверка статус кода ссылок на сайте: {link_url}'):
            assert response.status_code == expected_status_code, f'Статус код не равен {expected_status_code}. Статус код должен быть равен {response.status_code}'
