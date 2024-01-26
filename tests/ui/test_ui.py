import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#import time

@pytest.mark.ui 
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Відкриття сторінки htttps://github.com/login
    driver.get("https://github.com/login")

    # Пошук поля, в яке треба буде ввести неправильне ім'я користувача або емейл
    login_elem = driver.find_element(By.ID, "login_field")

    # Ввід неправильного імені користувача або емейла
    login_elem.send_keys("sergiibutenko@mistakenemail.com")
    #time.sleep(3)

    # Пошук поля, в яке треба буде ввести неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")
    
    # Ввід неправильного пароля
    pass_elem.send_keys("wrong password")
    #time.sleep(3)

    # Пошук кнопки "Sign in"
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емуляція кліка лівоб кнопкою миши
    btn_elem.click()
    
    # Перевірка, що назва сторінки така, як очікується
    assert driver.title == "Sign in to GitHub · GitHub"
    #time.sleep(3)

    # Закриття браузера
    driver.close()