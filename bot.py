from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello world"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    if 'start' in incoming_msg:
        msg.body("Hello, I'm a simple whatsapp echobot. I echo any message you send me, please give it a try.")
    else:
        msg.body(incoming_msg)
    return str(resp)

if __name__ == '__main__':
    app.run()
