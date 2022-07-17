from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
from pytube import YouTube
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello world"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    if incoming_msg=='hi'or incoming_msg=='Hi' or incoming_msg=='HI' or incoming_msg=='hI' :
        msg.body("*Hello, I'm a simple whatsapp echobot. I echo any message you send me, please give it a try*.")
        msg.body('This bot programme by senupama isuranda...🙂')
        msg.media('https://raw.githubusercontent.com/senupama/whatsapp-echobot/main/hi-there-inscription-handwritten-lettering-illustration-black-vector-text-speech-bubble-simple-outline-marker-style-hi-there-194142459.jpg')
    if incoming_msg=='bot_name':
        msg.body('*i am whatsapp echo bot*')
        msg.media('https://raw.githubusercontent.com/senupama/whatsapp-echobot/main/bot.png')
    if incoming_msg=='youtube':
            url=msg.body("enter your video link")
            msg.body('Title = '+str(url.title))
            
    result=[1,2,3,4]
    if incoming_msg=='fgh':
      msg=res.message(str(result[0]))
      msg=res.message(str(result[1])
 
    
    return str(resp)

if __name__ == '__main__':
    app.run()
