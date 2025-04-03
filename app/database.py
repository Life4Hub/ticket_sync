import mysql.connector
from mysql.connector import Error

def handle_db_error(func):
    """Decorator to handle database errors."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    return wrapper

@handle_db_error
def init_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2308",
        database="ticket_sync"  # Datenbankname angepasst
    )
    if connection.is_connected():
        print("Connected to the database.")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            system_name VARCHAR(255) NOT NULL,
            status VARCHAR(255) NOT NULL,
            comments TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connection.commit()
    print("Table 'tickets' ensured to exist.")
    cursor.close()
    connection.close()
    print("MySQL connection is closed.")

@handle_db_error
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2308",
        database="ticket_sync"  # Datenbankname angepasst
    )
