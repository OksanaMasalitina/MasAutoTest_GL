import pytest
from modules.api.clients.github import GitHub
import requests
import os


# Фікстура для створення екземпляру класу GitHub
@pytest.fixture
def github_api():
    api = GitHub()
    yield api


# Фікстура для запису у файл хеша останнього коміту 
@pytest.fixture
def save_last_commit_hash_file():
    def _save_last_commit_hash(commit_hash):
        filename = "last_commit_hash.txt"
        with open(filename, "w") as file:
            file.write(commit_hash)
            print("Нове значення last_commit_hash збережено")
    return _save_last_commit_hash


# Фікстура для отримання хеша останнього коміту, який був збережений у файлі 
@pytest.fixture
def last_commit_hash_file():
    filename = "last_commit_hash.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            last_commit_hash = file.read().strip()
            print("Значення last_commit_hash:", last_commit_hash)
            return last_commit_hash
    else:
        print("Файл last_commit_hash.txt не існує.")
        return None


# Фикстура для видалення коментаря до коміту
@pytest.fixture
def delete_comment():
    def _delete_comment(owner, repo, comment_id):
        github_token = os.getenv('GITHUB_TOKEN')
        if not github_token:
            raise ValueError("GitHub token  не налаштовано. Додайте токен у змінну середовища")
            
        url = f"https://api.github.com/repos/{owner}/{repo}/comments/{comment_id}"

        headers = {
                "Authorization": f"token {github_token}",
                "Accept": "application/vnd.github.v3+json"
            }

        response = requests.delete(url, headers=headers)
        return response.status_code
    return _delete_comment



class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None
    
    def create(self):
        self.name = 'Oksana'
        self.second_name = 'Masalitina'
    
    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()  

