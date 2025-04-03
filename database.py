import mysql.connector

def init_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2308",
        database="ticket_sync"
    )
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
    connection.close()

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2308",
        database="ticket_sync"
    )
