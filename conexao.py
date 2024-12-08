import mysql.connector
from mysql.connector import errorcode

try:
    # Tenta conectar ao banco de dados
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='mydatabase'
    )
    print("Database connection made!")

except mysql.connector.Error as error:
    # Verifica se o erro é que o banco de dados não existe
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist. Creating now...")
        try:
            # Conecta ao MySQL sem especificar um banco de dados
            db_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root'
            )
            cursor = db_connection.cursor()
            cursor.execute("CREATE DATABASE mydatabase")
            print("Database 'mydatabase' created successfully!")
        except mysql.connector.Error as create_error:
            print(f"Failed to create database: {create_error}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'db_connection' in locals() and db_connection.is_connected():
                db_connection.close()
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(error)

else:
    db_connection.close()
