from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(SignInPage.URL)
    
    def try_login(self, username, password):
        # Пошук поля, в яке треба буде ввести неправильне ім'я користувача або емейл
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Ввід неправильного імені користувача або емейла
        login_elem.send_keys(username)

        # Пошук поля, в яке треба буде ввести неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")
    
        # Ввід неправильного пароля
        pass_elem.send_keys(password)
   
        # Пошук кнопки "Sign in"
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емуляція кліка лівоб кнопкою миші
        btn_elem.click()
    
    def check_title(self, expected_title): 
        return self.driver.title == expected_title
