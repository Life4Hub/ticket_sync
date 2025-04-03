
from flask import Flask, request, jsonify
from app.database import init_db, save_ticket_data

app = Flask(__name__)
init_db()

@app.route("/ticket", methods=["POST"])
def sync_ticket():
    data = request.json
    print("Empfangene Daten:", data)

    if not data.get("ticket_id"):
        return jsonify({"error": "ticket_id fehlt"}), 400

    save_ticket_data(data)
    return jsonify({"status": "erfolgreich gespeichert"}), 200
