# db.py
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    """Fonction pour se connecter à la base de données MySQL."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='scrapping'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connecté à MySQL Server version {db_info}")
            return connection
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL {e}")
        return None
