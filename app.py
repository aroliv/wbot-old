from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Pasta onde o arquivo CSV será armazenado
csv_folder = 'csv_data'

# Função para criar um arquivo CSV se ele não existir e salvar as interações
def save_interaction(phone_no, message, timestamp):
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    csv_file = os.path.join(csv_folder, 'interactions.csv')

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([phone_no, message, timestamp])
        
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)