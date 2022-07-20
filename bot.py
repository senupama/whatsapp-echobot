from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello world"

@app.route('/bot', methods=['POST'])
def bot():
    user_msg = request.form.get('Body') 
    print("user_msg------"+str(user_msg))
    s=input('enter your name = ')
    print(s)
    # creating object of MessagingResponse
    response = MessagingResponse()
    reply=response.message()
    if user_msg=='hi':
        reply.body('*hello!* ')
        reply.media('https://raw.githubusercontent.com/senupama/whatsapp-echobot/main/hi-there-inscription-handwritten-lettering-illustration-black-vector-text-speech-bubble-simple-outline-marker-style-hi-there-194142459.jpg')
    try: # Storing the file that user send to the Twilio whatsapp number in our computer
        msg_url=request.form.get('MediaUrl0')  # Getting the URL of the file
        print("msg_url-->",msg_url)
        msg_ext=request.form.get('MediaContentType0')  # Getting the extension for the file
        print("msg_ext-->",msg_ext)
        ext = msg_ext.split('/')[-1]
        print("ext-->",ext)
        if msg_url != None:
            json_path = requests.get(msg_url)
            filename = msg_url.split('/')[-1]
            open(filename+"."+ext, 'wb').write(json_path.content)  # Storing the file
    except:
        print("no url-->>") 
    if user_msg=='hello':
        s=reply.body('hello')
        print(s)
     
    return str(response)

if __name__ == '__main__':
    app.run()
