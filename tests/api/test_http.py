import pytest
import requests

#Тест відправляє HTTP запит з методом GET на вказану адресу, 
#та за допомогою f-рядків виводить на екран атрибут text відповіді від сервера  

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

#Тест перевіряє, що атрибут name тіла відповіді відповідає значенню ‘Chris Wanstrath’, 
#статус код 200, заголовок Server  - ‘GitHub.com’
@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert body['followers'] == 22243
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'
    assert headers['Content-Length'] != '500'
    assert headers['x-github-api-version-selected'] < '2023-01-01'

#Тест відправляє HTTP запит з методом GET на відповідну адресу та перевіряє що статус код - 404
@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/oksana_masalitina')

    assert r.status_code == 404