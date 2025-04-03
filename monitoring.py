import smtplib
from email.mime.text import MIMEText

def send_error_notification(error_message):
    sender = "admin@example.com"
    recipient = "admin@example.com"
    subject = "Ticket Sync Error Notification"
    body = f"An error occurred: {error_message}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP('localhost') as server:
        server.sendmail(sender, recipient, msg.as_string())
