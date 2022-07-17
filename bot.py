from flask import Flask, request
import requests
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello world"

@app.route('/bot', methods=['POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()
  
    # creating object of MessagingResponse
    response = MessagingResponse()
    reply=response.message()
    if user_msg=='hi':
        reply.body('*hello!*')
        reply.media('https://raw.githubusercontent.com/senupama/whatsapp-echobot/main/hi-there-inscription-handwritten-lettering-illustration-black-vector-text-speech-bubble-simple-outline-marker-style-hi-there-194142459.jpg')
        
    return str(response)

if __name__ == '__main__':
    app.run()
