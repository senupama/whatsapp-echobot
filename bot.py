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
    if incoming_msg=='hi'or incoming_msg=='Hi' or incoming_msg=='HI' or incoming_msg=='hI' :
        msg.body("Hello, I'm a simple whatsapp echobot. I echo any message you send me, please give it a try.")
        
        msg.body('This bot programme by senupama isuranda...🙂')
    else:
        msg.body('wrong type '+str(incoming_msg))
    return str(resp)

if __name__ == '__main__':
    app.run()
