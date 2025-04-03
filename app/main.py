from flask import Flask
from app.database import init_db

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Ticket Sync API!"

if __name__ == '__main__':
    init_db()  # Datenbank initialisieren
    app.run(debug=True)
