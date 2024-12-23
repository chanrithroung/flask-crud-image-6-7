import pymysql


DB_HOST = '127.0.0.1' # or you can use: localhost
DB_USER = 'root'
DB_PASSWORD = '24022004'
DB_NAME = 'flask_crud_image_6_7'


def db_connect():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
    )

    query = f"CREATE DATABASE IF NOT EXISTS  {DB_NAME}"  

    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print(f"Database {DB_NAME} created successfully")
        
    except pymysql.MySQLError as e:
        print(f"Error creating database: {e}")

    cursor.execute(f"USE {DB_NAME}")

    return connection



if __name__ == '__main__':
    db_connect()