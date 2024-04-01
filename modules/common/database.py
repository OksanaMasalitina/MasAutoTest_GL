import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/oksana/Masalitina_AutoTestGL' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()
    

    def close_connection(self):
        self.connection.close()
    

    # Метод для перевірки підключення до бази даних
    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
    

    # Метод для отримання інформації про всіх покупців (коротка версія)
    def get_all_users_short(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record  
    

    # Метод для отримання інформації про всіх покупців (повна версія)
    def get_all_users_full(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 
    

    # Метод для пошуку дублікатів записів про покупців по комбінації імені, адреси та міста
    def search_duplicates(self):
        query = f'''
            SELECT name, address, city, COUNT(*) 
            FROM customers 
            GROUP BY name, address, city 
            HAVING COUNT(*) > 1
        '''
        self.cursor.execute(query)
        duplicates = self.cursor.fetchall()

        return duplicates


    # Перевірка даних у таблиці "Продукти"
    def get_all_products(self):
        query = f'''
            SELECT * 
            FROM products
        '''
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 
    

    # Метод для отримання інформації про всі замовлення
    def get_all_orders(self):
        query = f'''
            SELECT * 
            FROM orders
        '''
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record  
    
    
    # Вставка нового рядка до таблиці "Покупці"
    def insert_customer(self, id, name, address, city, postalCode, country):
        query = f'''
            INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country)
            VALUES ({id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}' )            
        '''
        self.cursor.execute(query)
        self.connection.commit()

    
    # Вставка нового рядка до таблиці "Покупці" (без replace)
    def insert_unic_customer(self, id, name, address, city, postalCode, country):
        query = f'''
            INSERT INTO customers (id, name, address, city, postalCode, country)
            VALUES ({id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}' )            
        '''
        self.cursor.execute(query)
        self.connection.commit()


     # Вставка нового рядка до таблиці "Продукти"
    def insert_product(self, product_id, name, description, qnt):
        query = f'''
            INSERT OR REPLACE INTO products (id, name, description, quantity)
            VALUES ({product_id}, '{name}', '{description}', {qnt})            
        '''
        self.cursor.execute(query)
        self.connection.commit()

    
    # Вставка нового рядка до таблиці "Замовлення"
    def insert_order(self, id, customer_id, product_id, order_date):
        query = f'''
            INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date)
            VALUES ({id}, {customer_id}, {product_id}, '{order_date}')            
        '''
        self.cursor.execute(query)
        self.connection.commit()

    
    # Отримати інформацію про напізніше замовлення
    def get_the_last_order(self):
        query = f'''
            SELECT order_date
            FROM orders
            ORDER BY order_date DESC
            LIMIT 1
        '''
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    # Метод для отримання адреси покупця за його ім'ям
    def get_user_address_by_name(self, name):
        query = f'''
            SELECT address, city, postalCode, country 
            FROM customers 
            WHERE name = '{name}'
        '''
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    # Метод для оновлення кількості певного продукту
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f'''
            UPDATE products 
            SET quantity = {qnt}
            WHERE id = {product_id}
            '''
        self.cursor.execute(query)
        self.connection.commit()


    # Метод для отримання кільості певного продукту 
    #(для перевірки, що кількість певного продукту після оновлення змінилась)
    def select_product_qnt_by_id(self, product_id):
        query = f'''
            SELECT quantity
            FROM products 
            WHERE id = {product_id}
            '''
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    
    # Видалення рядка з таблиці "Покупці"
    def delete_customer_by_id(self, id):
        query = f"DELETE FROM customers WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()


    # Видалення рядка з таблиці "Продукти"
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    
    # Поєднання таблиць та отримання деталей замовлення
    def get_detalied_orders(self):
        query = '''
            SELECT orders.id, customers.name, customers.address, customers.city, products.name, 
                products.description, orders.order_date
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            JOIN products ON orders.product_id = products.id
            ORDER BY orders.order_date ASC
        '''
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record