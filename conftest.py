import pytest
from modules.api.clients.github import GitHub
import os


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


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def last_commit_hash_file():
    filename = "last_commit_hash.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            last_commit_hash = file.read().strip()
            print("last_commit_hash value:", last_commit_hash)
            return last_commit_hash
    else:
        print("Файл last_commit_hash.txt не існує.")
        return None

@pytest.fixture
def save_last_commit_hash_file():
    def _save_last_commit_hash(commit_hash):
        filename = "last_commit_hash.txt"
        with open(filename, "w") as file:
            file.write(commit_hash)
            print("last_commit_hash saved")
    return _save_last_commit_hash