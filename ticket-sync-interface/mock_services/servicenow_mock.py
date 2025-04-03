
import requests
import time

while True:
    print("Sende Test-Ticket an Schnittstelle...")
    response = requests.post("http://localhost:5000/ticket", json={
        "ticket_id": "SN-1234",
        "system": "ServiceNow",
        "status": "in Bearbeitung",
        "kommentar": "User meldet Problem mit VPN",
        "zeitstempel": "2025-04-03T09:30:00"
    })
    print(response.status_code, response.text)
    time.sleep(10)
