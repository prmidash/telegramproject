url='https://api.telegram.org/bot1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w/'
import requests
import json
def getupdates():
    all=requests.get(url+'getUpdates')
    return all.json()

def getlast(dic):
    return dic['result'][-1]

def chat_id(last):
    return last['message']['chat']['id']


def send_message(id,txt):
    send={'chat_id': id, 'text': txt }
    s=requests.post(url+'sendMessage',send)
    return s
    
while True:
    allmessage=getupdates()
    lastmessage=getlast(allmessage)
    chatid=chat_id(lastmessage)