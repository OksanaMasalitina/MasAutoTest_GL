import requests
import os

class GitHub:

    github_token = os.getenv('GITHUB_TOKEN')
    
    # Метод для отримання хешу останнього коміту до репозіторію
    def get_last_commit_hash(self, owner, repo):
        base_url = "https://api.github.com"
        url = f"{base_url}/repos/{owner}/{repo}/commits"
        r = requests.get(url)

        body = r.json()[0]
        new_commit_hash = body['sha'] 
        
        return new_commit_hash
    
    # Метод для створення коментаря до останнього коміту репозіторія 
    def add_comment_to_commit(self, owner, repo, commit_sha, comment):
        # Отримуємо токен змінної середовища
        github_token = os.getenv('GITHUB_TOKEN')
        if not github_token:
            raise ValueError("GitHub token  не налаштовано. Додайте токен у змінну середовища")
        
        base_url = "https://api.github.com"
        url = f"{base_url}/repos/{owner}/{repo}/commits/{commit_sha}/comments"

        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json" }
        data = {"body": comment}

        response = requests.post(url, headers=headers, json=data)

        return response
    

    # Метод для отримання кількості комітів до репозіторія
    def count_commits(self, owner, repo):
        base_url = "https://api.github.com"
        url = f"{base_url}/repos/{owner}/{repo}/commits"
        r = requests.get(url)

        total_commits = len(r.json())
        
        return total_commits
    

    # Метод для отримання даних про публічні репозіторії юзера
    def get_public_repositories(self, username):
        base_url = "https://api.github.com"
        url = f"{base_url}/users/{username}/repos"
        r = requests.get(url)

        body = r.json()

        return body
    

    # Метод для отримання даних про конкретний репозиторій юзера 
    def search_my_repo(self, username, name):
        base_url = "https://api.github.com"
        url = f"{base_url}/search/repositories"
        r = requests.get(url, params={"q": name, "login": username})
        
        body = r.json()

        return body
    

    # Метод для отримання даних про користувача
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        
        body = r.json()

        return body
    

    # Метод для отримання даних про репозіторій
    def search_repo(self, name):
        r = requests.get(
            'https://api.github.com/search/repositories', 
            params={"q": name})
        
        body = r.json()

        return body

    