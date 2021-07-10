import json
import requests
url = "https://api.telegram.org/bot1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w/"

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

def get_all_updates():
    response = requests.get(url + 'getUpdates')
    return response.json()

def get_last_update(allUpdates):
    return allUpdates['result'][-1]

def get_chat_id(update):
    return update['message']['chat']['id']

def sendMessage(chat_id , text):
    sendDate = {
        'chat_id' : chat_id
        'text' : text
    }
    response = requests.post(url + 'sendMessage' , sendDate)
    return response
@app.route('/' , methods = ['POST' , 'GET'])
def index():
    msg = request.get_json()
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = get_chat_id(msg)
        text = msg['message'].get('text' , '') #end of routins
        if text == '/start':
            sendMessage(chat_id , 'Welcome !')
        #username = msg['message']['from']['username']
        return Response('ok' , status = 200)
    else:
        return "<h1>Salam</h1>"
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
app.run(debug = True)










