import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert body['followers'] == 21757 
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'
    assert headers['Content-Length'] != '500'
    assert headers['x-github-api-version-selected'] < '2023-01-01'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/oksana_masalitina')

    assert r.status_code == 404