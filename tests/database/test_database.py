import pytest
from modules.common.database import Database
import sqlite3
from datetime import datetime


# Тест для перевірки підключення до бази даних
@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

# Тест для перевірки правильності роботи запиту отримання даних про всіх юзеров
@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users_short()

    print("Покупці:", users)
    db.close_connection()

# myTest
# Додавання нових користувачів та перевірка правильності додавання даних (користувавчі додані 
# також для розширення бази даних, тому наприкінці тесту не видаляються)
@pytest.mark.database
def test_customer_insert():
    db = Database()
    db.insert_customer(3, 'Oleksii', 'Peremohy av. 62D-77', 'Kharkiv','61210','Ukraine')
    db.insert_customer(4, 'Oleksii', 'Peremohy av. 62D-89', 'Kharkiv', '61210','Ukraine')
    db.insert_customer(5, 'Stepan', 'Obolonsky av. 10', 'Kyiv','04209','Ukraine')

    users = db.get_all_users_full()
    
    print("Покупці, повна інформація:", users)
    db.close_connection()

# myTest   
# Додати дані у таблицю "Замовлення" для розширення бази даних (до того вона мала недостатню 
# кількість записів для демонстрації виконання тестів)
@pytest.mark.database
def test_order_insert():
    db = Database()
    db.insert_order(2,1, 1, '10:19:22')
    db.insert_order(3,4, 2, '18:02:18')
    db.insert_order(4,4, 3, '11:33:09')
    db.insert_order(5,5, 1, '10:00:15')

# Переконатися що дані додані та подивитися деталі замовлення
    orders = db.get_detalied_orders()

    print("Замовлення:", orders)
    db.close_connection()

# myTest   
# Відсортувати найпізніше замовлення та перевірити, чи не було воно зроблене у неробочий час
@pytest.mark.database
def test_the_last_order():
    db = Database()
    last_order_time = db.get_the_last_order()
# Перетворення рядка на об'єкт datetime
    last_order_time = datetime.strptime(last_order_time[0][0], '%H:%M:%S').time()  
    
# Графік роботи магазину
    finish_time = datetime.strptime('21:00:00', '%H:%M:%S').time()

    assert last_order_time <= finish_time, "Замовлення зроблено в неробочий час"
    db.close_connection()

# myTest   
# Перевірка що при спробі вставити дані про покупця з вже існуючим id виникне помилка 
# (id взято як приклад, в реальних БД це може бути будь-який інший унікальний стовпець, 
# який задали, щоб уникнути дублікатів даних)
@pytest.mark.database
def test_duplicate_user_id():
    db = Database()
    user_id = 2

    try:
        # Спроба додати користувача з існуючим id
        db.insert_unic_customer(user_id, 'Oleksii', 'Khreshatyk 14/2', 'Kyiv','61210','Ukraine')
        
    except sqlite3.IntegrityError as e:
        # Перевірка, що виникла IntegrityError, що відповідає помилці унікальності
        print(f"Такий id вже існує, IntegrityError: {e}")  
    db.close_connection()


# myTest   
# Перевірка, що БД не містить дублікатів записів про покупців. Обрани колонки таблиці customers, а саме комбінація 
# імені, адреси та міста, за якими можна ствержувати, що ці дані належать одному тому самому покупцю. 
# Звісно це не зовсім так, але в рамках задачи припустимо.
@pytest.mark.database
def test_check_duplicates_data():
    db = Database()
    duplicates = db.search_duplicates()

    assert len(duplicates) == 0, f"Знайдені дублікати: {duplicates}"
    db.close_connection()


# myTest
# Перевірка, чи для всіх замовлень у нас є дані для доставки 
# (тобто немає null та порожніх значень в полях "адреса" та "місто")
@pytest.mark.database
def test_no_empty_address_or_city_in_orders():
    db = Database()
    orders = db.get_detalied_orders()

    # Перевірка, що у кожному замовленні чи є дані для доставки
    for order in orders:
        order_id, customer_name, address, city, product_name, product_description, order_date = order
        
        assert address is not None and address != '', f"Порожня адреса у замовленні {order_id}"
        assert city is not None and city != '', f"Порожнє місто у замовленні {order_id}"
        db.close_connection()

# Тест для перевірки отримання адреси покупця за його ім'ям
@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'
    db.close_connection()

# Тест для перевірки оновлення кількості певного продукту
@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25
    db.close_connection()

# Перевірка даних у таблиці "Продукти"
@pytest.mark.database
def test_check_all_products():
    db = Database()
    products = db.get_all_products()

    print("Товари:", products)
    db.close_connection()

# Додавання нового рядка та перевірка правильності додавання даних
@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30
    db.close_connection()


# Тест для перевірки коректності видалення даних
@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0
    db.close_connection()


# Тест для перевірки коректності поєднання таблиць та виведення деталей замовлення
@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detalied_orders()
    print("Замовлення", orders)
    # Перевірка что кількість замовлень равна 5
    assert len(orders) ==5
    db.close_connection()

    # Перевірка структури даних
    # Метод get_detalied_orders було відозмінено мною для універсальності використання у 
    # інших моїх тестах, тому структура даних теж змінилась. 
    assert orders[0][0] == 5
    assert orders[0][1] == 'Stepan'
    assert orders[0][2] == 'Obolonsky av. 10'
    assert orders[0][3] == 'Kyiv'
    assert orders[0][4] == 'солодка вода' 
    assert orders[0][5] == 'з цукром'
    assert orders[0][6] == '10:00:15' 

    db.close_connection()
    