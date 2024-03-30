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
    assert r['total_count'] == 56
    assert 'become-qa-auto' in r['items'][0]['name']


#перевірка що репозиторія не існує
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('oksanamasalitina_non_existing_repo')
    assert r['total_count'] == 0


#перевірка що існує репозиторій з довжиною імені в 1 символ
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('u')
    assert r['total_count'] != 0

#перевірка що існує конкретний репозиторій конкретного юзера 
@pytest.mark.api
def test_my_repo_count(github_api):
    r = github_api.search_my_repo(username ='KsanaMasss', name = 'KsanaRep1')
    #print(r)
    assert r != 0


#перевірка що у юзера є публічні репозіторії
@pytest.mark.api
def test_user_have_public_repo(github_api):
    r = github_api.get_public_repositories(username ='KsanaMasss')
    #print(r)
    assert r != 0


#отримання хешу останнього коміту публічного репозіторія
@pytest.mark.api
def test_last_commit_hash(github_api, last_commit_hash_file, save_last_commit_hash_file):
    commit_hash = github_api.get_last_commit_hash(owner='OksanaMasalitina', repo='MasAutoTest_GL', last_commit_hash_file=last_commit_hash_file, save_last_commit_hash_file=save_last_commit_hash_file)
    print(commit_hash)
    