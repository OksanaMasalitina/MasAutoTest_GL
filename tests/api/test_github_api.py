import pytest


# Перевірка, що за період від попереднього проходження тесту, в репозіторії не з'явилося нових комітів
@pytest.mark.api
def test_last_commit_hash(github_api, last_commit_hash_file, save_last_commit_hash_file):
    new_commit_hash = github_api.get_last_commit_hash(owner='OksanaMasalitina', repo='MasAutoTest_GL')
    if last_commit_hash_file != new_commit_hash:
        save_last_commit_hash_file(new_commit_hash)
        print("Знайдено новий коміт. Новий хеш збережено")
        assert False 
    else:
        print("Немає нових комітів")

        assert True 


# Перевірка успішного додавання коментаря до останнього коміту + видалення коментаря
@pytest.mark.api
def test_add_comment_to_commit(github_api,last_commit_hash_file, delete_comment):
    comment = "Мій новий коментар до останнього коміту"

    new_comment = github_api.add_comment_to_commit(owner='OksanaMasalitina', repo='MasAutoTest_GL', commit_sha=last_commit_hash_file, comment=comment)
    
    assert new_comment.status_code == 201

    comment_id = new_comment.json().get('id')
    if comment_id:
        delete_status_code = delete_comment(owner='OksanaMasalitina', repo='MasAutoTest_GL', comment_id=comment_id)
        assert delete_status_code == 204
        
    
# Перевірка кількості комітів до репозіторія
@pytest.mark.api
def test_commit_count(github_api):
    r = github_api.count_commits(owner='OksanaMasalitina', repo='MasAutoTest_GL')
    
    print("Всього комітів:", r)

    assert r >= 25


# Перевірка, що у юзера є публічні репозіторії
@pytest.mark.api
def test_user_have_public_repo(github_api):
    r = github_api.get_public_repositories(username ='KsanaMasss')
    
    assert r != 0


# Перевірка, що у юзера існує конкретний репозиторій
@pytest.mark.api
def test_my_repo_count(github_api):
    r = github_api.search_my_repo(username ='KsanaMasss', name = 'KsanaRep1')

    assert r != 0


# Перевірка, що юзер існує
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    
    assert user['login'] == 'defunkt'


# Перевірка, що юзера не існує
@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('Masalitina_Ksana')
    
    assert r['message'] == 'Not Found'


# Перевірка, що конкретний репозиторій існує
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    
    assert r['total_count'] == 56
    assert 'become-qa-auto' in r['items'][0]['name']


# Перевірка, що репозиторія не існує
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('oksanamasalitina_non_existing_repo')
    
    assert r['total_count'] == 0


# Перевірка, що існує репозиторій з довжиною імені в 1 символ
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('u')
    
    assert r['total_count'] != 0
    