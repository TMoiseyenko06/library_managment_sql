import mysql.connector as connector
from mysql.connector import Error

def connect():
    try:
        conn = connector.connect(
            database = 'library_data',
            user = 'root',
            password = '',
            host ='localhost'
        )
        if conn.is_connected():
            return conn
    except Error:
        return None