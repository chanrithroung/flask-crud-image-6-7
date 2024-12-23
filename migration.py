from db_connect import db_connect
from pymysql import MySQLError

def creat_table():
    query = """
        CREATE TABLE IF NOT EXISTS products(
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            product_price FLOAT NOT NULL,
            thumbnail VARCHAR(255),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """

    connection = db_connect()
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print("Table products created successfully")
    except MySQLError as error:
        print(f"Error creating table: {error}")



creat_table()
