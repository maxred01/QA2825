import pytest
import requests
import json
import allure


BASE_URL = "https://tryhackme.com"

AUTH_HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'referer': 'tryhackme.com',
    'Cookie': 'thm-aid=d5b8b804-9cc3-49b2-9111-191fe521cbdc; _csrf=Crp4lO3dAc3fxi9Py_pcnaAF; _hjSessionUser_1950941=eyJpZCI6IjUzYmEzOWEwLTFkZjEtNWY5MS1hMzQ3LWQ3MDk4ZDY1MDExNyIsImNyZWF0ZWQiOjE3NjM5ODQ4OTc3MjQsImV4aXN0aW5nIjp0cnVlfQ==; ajs_anonymous_id=d5b8b804-9cc3-49b2-9111-191fe521cbdc; _ga=GA1.1.893520014.1763984899; thm-amplitude-device-id=d5b8b804-9cc3-49b2-9111-191fe521cbdc; ajs_user_id=687e46b8ad61437da3d8465f; hubspotutk=aeb59721d6eb4bfc527d839d0ca11943; __hssrc=1; intercom-device-id-pgpbhph6=8e7254ee-b540-4c9e-9c1c-f595ac910c67; cookieconsent_status=dismiss; thm-amplitude-session-id=1763549969612; analytics_session_id=1763549969612; connect.sid=s%3AEyWFQNcJ_NJoxKv3WlWsvUJ00Ra-RX01.jLP77SOFB9ZEUxGobofVlkDPVc9BtSvWqKudc%2FcYCao; gbStickyBuckets__anonymousId||d5b8b804-9cc3-49b2-9111-191fe521cbdc={%22attributeName%22:%22anonymousId%22%2C%22attributeValue%22:%22d5b8b804-9cc3-49b2-9111-191fe521cbdc%22%2C%22assignments%22:{%22is-french-language__0%22:%220%22%2C%22new-homepage__0%22:%220%22%2C%22google-one-tap-auto-login__1%22:%220%22%2C%22linkedin-social-login__0%22:%220%22}}; _hjSession_1950941=eyJpZCI6IjRmODE4NjczLWVmOTctNGY1Yy04OWVkLTQ3NzdjZGIxNmRjNCIsImMiOjE3NjQzMzgyNTU1MDIsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __hstc=256179476.aeb59721d6eb4bfc527d839d0ca11943.1763984900371.1764328170640.1764338261090.20; g_state={"i_l":0,"i_ll":1764339407284,"i_b":"5LppW8iJc1d4dF9SVDfMb5vsSSiltmO5ibjVopQ+IYU"}; _rdt_uuid=1763984898372.16495a5b-cbce-4f18-a720-15c098241782; analytics_session_id=1763549969612; __hssc=256179476.2.1764338261090; _gcl_au=1.1.1014173419.1763984898.880071405.1764339411.1764339439; logged-in-hint=687e46b8ad61437da3d8465f; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22Asperatus.%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D; _cioid=687e46b8ad61437da3d8465f; _rdt_em=:e9aff251222f82b670e8d33ac5b56e59dbaa79bab3ee91d10af3f3b55a61ba6b; gbStickyBuckets__id||687e46b8ad61437da3d8465f=%7B%22attributeName%22%3A%22id%22%2C%22attributeValue%22%3A%22687e46b8ad61437da3d8465f%22%2C%22assignments%22%3A%7B%22signup-flash-sale__6%22%3A%220%22%2C%22improvement-offensive-security-intro__0%22%3A%220%22%7D%7D; intercom-session-pgpbhph6=U242Yi94ZGtSakNkSWYrcnZIYm12TEN0dUZPa0VqWnFSYUdvWjJnU2pUZ1NlRFRuNlg2NHI2azQ2VjloMUR1L1pUMCs1OHF5TGswa0t0cGIvZ1M0aVNMajRCRitlcHBpeUJydXRkd01ZQ1k9LS1aRm1lVWdUWGpuNFRGZ1pRanlCcUtnPT0=--65015870614cefa90521591c9783091c87f15d9d; _hjHasCachedUserAttributes=true; analytics_session_id.last_access=1764340279716; _ga_Z8D4WL3D4P=GS2.1.s1764338251$o24$g1$t1764340280$j60$l0$h0; logged-in-hint=687e46b8ad61437da3d8465f; thm-aid=d5b8b804-9cc3-49b2-9111-191fe521cbdc; thm-ud=%7B%22id%22%3A%22687e46b8ad61437da3d8465f%22%2C%22experience%22%3A%22unset%22%2C%22isStudent%22%3Atrue%2C%22dateSignUp%22%3A%222025-07-21T13%3A55%3A04.339Z%22%2C%22email%22%3A%22talako00%40mail.ru%22%2C%22username%22%3A%22Asperatus.%22%2C%22country%22%3A%22by%22%2C%22howHeard%22%3A%22social_media%22%2C%22isPremium%22%3Afalse%7D'
# Срок действия куки живёт до 5 декабря, после надо будет заменить
}

@allure.epic('Тестирование API TryHackMe')
@allure.feature('Детали комнаты')
@allure.story('Доступ к деталям комнаты для аутентифицированного пользователя')
@pytest.mark.api
@pytest.mark.functional
def test_get_room_details_authenticated():
    room_code = 'picklerick'
    base_api_url = f'{BASE_URL}/api/v2/rooms/details'
    params = {'roomCode': room_code}

    print(f'\nТестируемый URL: {base_api_url} с параметром {params}')
    with allure.step(f'Отправка GET запроса к {base_api_url} с параметром {params}'):
        response = requests.get(base_api_url, headers=AUTH_HEADERS, params=params)

    with allure.step('Проверка статус-кода HTTP 200 OK'):
        assert response.status_code == 200, \
            f'Ожидался статус-код 200, получен {response.status_code}. Тело ответа:\n{response.text[:500]}'
    with allure.step('Декодирование ответа JSON'):
        try:
            data = response.json()
            print('Ответ успешно декодирован как JSON')
        except requests.exceptions.JSONDecodeError as e:
            pytest.fail(
                f'Не удалось декодировать ответ как JSON. Ошибка: {e}\n'
                f'Полное тело ответа сервера:\n{response.text[:500]}'
            )
            return
    with allure.step('Проверка статуса ответа API ("success")'):
        assert data.get('status') == 'success', f'API вернуло статус ошибки: {data.get("status")}'

    room_data = data.get('data')
    with allure.step('Проверка наличия вложенного ключа "data"'):
        assert room_data is not None, "В ответе API отсутствует вложенный ключ 'data'"

    room_title = room_data.get('title')
    expected_titles = ['Pickle Rick']
    with allure.step(f'Проверка названия комнаты: {room_title}'):
        assert room_title in expected_titles, f"Неверное название комнаты. Ожидалось одно из {expected_titles}, получено '{room_title}'"

    with allure.step('Проверка сложности комнаты (easy)'):
        assert 'difficulty' in room_data, "Отсутствует ключ 'difficulty'"
        assert room_data.get('difficulty') == 'easy', 'Неверная сложность комнаты'

    with allure.step('Проверка типов данных основных атрибутов'):
        assert isinstance(room_data.get('code'), str), 'Код комнаты должен быть строкой'
        assert isinstance(room_data.get('users'), int), 'Количество пользователей должно быть целым числом'
        assert isinstance(room_data.get('freeToUse'), bool), 'Флаг freeToUse должен быть булевым значением'

    with allure.step('Проверка списка создателей (наличие и тип)'):
        assert 'creators' in room_data, 'Отсутствует список создателей'
        assert isinstance(room_data['creators'], list), 'Создатели должны быть списком'
        assert len(room_data['creators']) > 0, 'Список создателей не должен быть пустым'

    with allure.step('Проверка наличия автора "tryhackme" в списке'):
        creator_usernames = [creator.get('username') for creator in room_data['creators']]
        assert 'tryhackme' in creator_usernames, 'Пользователь "tryhackme" не найден в списке создателей'

    with allure.step('Проверка статуса публичности комнаты'):
        assert room_data.get('public') is True, 'Комната должна быть публичной'

    with allure.step('Проверка типа IP-адреса (private)'):
        assert room_data.get('ipType') == 'private', 'Ожидался ipType: private'
