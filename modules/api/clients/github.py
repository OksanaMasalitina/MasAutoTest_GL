import requests

class GitHub:
    def __init__(self):
        self.last_commit_hash = None

    #метод для отримання даних про користувача
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    #метод для отримання даних про репозіторій
    def search_repo(self, name):
        r = requests.get(
            'https://api.github.com/search/repositories', 
            params={"q": name}
        )
        body = r.json()

        return body


    #метод для отримання даних про конкретний репозиторій конкретного юзера 
    def search_my_repo(self, username, name):
        r = requests.get(
            'https://api.github.com/search/repositories', 
            params={"q": name, "login": username}
        )
        body = r.json()

        return body
    

    #метод для отримання даних про публічні репозіторії юзера
    def get_public_repositories(self, username):
        base_url = "https://api.github.com"
        url = f"{base_url}/users/{username}/repos"
        r = requests.get(url)

        body = r.json()

        return body


    #метод для отримання кількості комітів до репозіторію
    '''def get_commits_count(self, owner, repo):
        base_url = "https://api.github.com"
        url = f"{base_url}/repos/{owner}/{repo}/commits"
        params = {'per_page': 1}  # Отримати лише 1 коміт для отримання загальної кількості

        r = requests.get(url, params=params)

        if r.status_code == 200:
            #return int(r.headers['X-Total-Count'])
            return r.headers
        else:
            print(f"Request failed with status code: {r.status_code}")
            return None'''
        
    #метод для отримання хешу останнього коміту до репозіторію
    '''def get_last_commit_hash(self, owner, repo):
        base_url = "https://api.github.com"
        url = f"{base_url}/repos/{owner}/{repo}/commits"
        r = requests.get(url)

        last_commit = r.json()[0]  
        #return last_commit['sha']
        self.last_commit_hash = last_commit['sha']  # Збереження останнього хешу коміту
        return self.last_commit_hash
    
    
    def get_last_commit_hash(self, owner, repo):
        base_url = "https://api.github.com"
        url = f"{base_url}/repos/{owner}/{repo}/commits"
        r = requests.get(url)

       
        last_commit = r.json()[0]
        new_commit_hash = last_commit['sha'] 

        if self.last_commit_hash is None:
            self.last_commit_hash = new_commit_hash  
            print("Хеш останнього коміту ініціалізовано.")
        elif self.last_commit_hash != new_commit_hash:
            self.last_commit_hash = new_commit_hash  
            print("Хеш останнього коміту змінився. Оновлено значення.")
        else:
            print("Хеш останнього коміту не змінився.")

        return self.last_commit_hash
    '''

    def get_last_commit_hash(self, owner, repo, last_commit_hash_file, save_last_commit_hash_file):
        base_url = "https://api.github.com"
        url = f"{base_url}/repos/{owner}/{repo}/commits"
        r = requests.get(url)

        last_commit = r.json()[0]
        new_commit_hash = last_commit['sha'] 

        
        if last_commit_hash_file != new_commit_hash:
            save_last_commit_hash_file(new_commit_hash)
            print("Хеш останнього коміту змінився. Оновлено значення.")
            return new_commit_hash
        else:
            print("Хеш останнього коміту не змінився.")

            return last_commit_hash_file