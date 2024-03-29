import requests

class GitHub:
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
    def get_public_repositories(username):
        base_url = "https://api.github.com"
        url = f"{base_url}/users/{username}/repos"
        r = requests.get(url)