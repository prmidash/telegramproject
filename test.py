import json
import requests
from flask import Flask
from flask import request
from flask import Response
import os

url = "https://api.telegram.org/bot1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w/ "
heroku = "setWebhook?url=https://fluid-mechanic.herokuapp.com/"

app = Flask(__name__)
r = {}
r['Reynolds'] = []
def get_all_updates():
    all = requests.get(url + 'getUpdates')
    return all.json()

def get_last_update(allUpdates):
    return allUpdates['result'][-1]

def get_chat_id(update):
    return update['message']['chat']['id']

def sendMessage(chat_id , text):
    sendDate = {'chat_id' : chat_id ,'text' : text,}
    response = requests.post(url + 'sendMessage' , sendDate)
    return response

def sendPhoto(chat_id , photo):
    sendData = {'chat_id' : chat_id , 'photo' : photo}
    response = requests.post(url + 'sendPhoto' , sendData)
    return response

@app.route('/' , methods = ['POST' , 'GET'])

def index():
    msg = request.get_json()
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = get_chat_id(msg)
        text = msg['message'].get('text' , '')
        if text == '/start':
            sendMessage(chat_id , 'Hi {}! Enter your request:\n/Firiction_factor\n/Show\n/Help'.format(msg['message']['chat']['first_name']))
        elif text == '/friction_factor':
            sendMessage(chat_id , "Enter the Reynold's number")
        #username = msg['message']['from']['username']
        return Response('ok' , status = 200)
    else:
        return '<h1 style="blinking;text-align:center;color: ##663399;" ><Blink>Hello Dear Chemical Engineer!</Blink></h1>'
def write_json(data , filename = 'contactlist.json'):
    with open(filename , 'w') as target:
        json.dump(data , target , indent=4 , ensure_ascii=False)
def read_json(filename = 'contactlist.json'):
    with open(filename , 'r') as target:
        data = json.load(target)
#while True:
#    data = get_all_updates()
#    lastUpdate = get_last_update(data)
#    sendMessage(get_chat_id(lastUpdate) , 'khobam')
write_json({})
app.run(host= "0.0.0.0" , port=int(os.environ.get('PORT' , 5000)))