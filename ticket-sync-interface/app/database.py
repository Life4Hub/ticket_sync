
import sqlite3

def init_db():
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT,
            system TEXT,
            status TEXT,
            kommentar TEXT,
            zeitstempel TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_ticket_data(data):
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO tickets (ticket_id, system, status, kommentar, zeitstempel)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data["ticket_id"],
        data.get("system", "unbekannt"),
        data.get("status", ""),
        data.get("kommentar", ""),
        data.get("zeitstempel", "")
    ))
    conn.commit()
    conn.close()
