import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.ui
def test_searching_product_and_adding_to_cart():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Відкриття головної сторінки сайту https://golka.com.ua
    driver.get("https://golka.com.ua")

    # Пошук поля, в яке треба буде ввести назву товару
    search_elem = driver.find_element(By.ID, "input_search")
   
    # Ввід назви товару "Пташка в гнізді"
    search_elem.send_keys("Пташка в гнізді")

    # Натискання клавіші Enter
    search_elem.send_keys(Keys.RETURN)
    
    #Очікування завантаження результатів пошуку 
    product_bird_elem = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='rm-module-title']/a[contains(text(), 'Пташка в гнізді')]")))

    # Знаходимо у результатах пошуку потрібний товар
    product_bird_elem = driver.find_element(By.XPATH, "//div[@class='rm-module-title']/a[contains(text(), 'Пташка в гнізді')]")
   
    # Відкриваємо сторінку зі знайденим товаром
    product_bird_elem.click()

    # Перевірка, що знаходимось на сторінці потрібного товару
    expected_url = "https://golka.com.ua/beadwork/embroidery-beads/biser-brooch/broshky-byserom/bp-314-brosh-ptichka-v-gnezde-crystal-art-nabor-dlya-vishivki-biserom.html"
    assert driver.current_url == expected_url

    # Пошук кнопки додавання товару "Пташка в гнізді" до кошику
    button_cart_elem = driver.find_element(By.ID, "button-cart")

    # Клік кнопки додавання в кошик
    button_cart_elem.click()

    # Чекати на відображення модального вікна за його класом 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-title")))

    # Перевірка, що модальне вікно містить кнопку "Оформити замовлення" (пошук кнопки за лінком)
    button_order_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Оформити замовлення")))
    
    # Клік на знайдену кнопку
    button_order_elem.click()
    
    # Пауза, щоб насолодитися результатом)
    time.sleep(3)

    # Закриття браузера
    driver.close()


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

    # Пошук поля, в яке треба буде ввести неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")
    
    # Ввід неправильного пароля
    pass_elem.send_keys("wrong password")

    # Пошук кнопки "Sign in"
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емуляція кліка лівою кнопкою миши
    btn_elem.click()
    
    # Перевірка, що назва сторінки така, як очікується
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриття браузера
    driver.close()


