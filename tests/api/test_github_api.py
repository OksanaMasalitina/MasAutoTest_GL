import pytest


#перевірка що юзер існує
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


#перевірка що юзера не існує
@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('Masalitina_Ksana')
    assert r['message'] == 'Not Found'


#перевірка що конкретний репозиторій існує
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']


#перевірка що репозиторія не існує
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('oksanamasalitina_non_existing_repo')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('8')
    assert r['total_count'] != 0

'''
# Перевірити, що один конкретний репозіторій існує
@pytest.mark.api
def test_my_repo_is_exist(github_api):
    r = github_api.search_repo('homepage')
    assert r['total_count'] != 0
    

@pytest.mark.api
def test_my_repo_count(github_api):
    r = github_api.search_my_repo(username ='KsanaMasss', name = 'KsanaRep1')
    print(r)
    assert r != 0

'''