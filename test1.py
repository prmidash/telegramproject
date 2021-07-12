import json
import requests
import fluids
#import flask
from flask import Flask
from flask import request
from flask import Response
import os

url = "https://api.telegram.org/bot1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w/"
app = Flask(__name__)
def getupdates():
    all = requests.get(url + 'getUpdates')
    return all.json()

def getlast(allUpdates):
    return allUpdates['result'][-1]

def chat_id(update):
    return update['message']['chat']['id']

def sendMessage(chat_id , text):
    send = {'chat_id' : chat_id ,'text' : text}
    response = requests.post(url + 'sendMessage' , send)
    return response

def sendPhoto(chat_id , photo):
    sendData = {'chat_id' : chat_id , 'photo' : photo}
    response = requests.post(url + 'sendPhoto' , sendData)
    return response
    

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        msg=request.get_json()
        chatid=chat_id(msg)
        sent=msg['message'].get('text','')
        if sent=='/start':
            sendMessage(chatid,"Hi {}! Enter your request:\n/Firiction_factor\n/Reynolds".format(msg['message']['chat'].get('first_name')))
        elif '/Firiction' in sent:
            m=0
            sendMessage(chatid,"Enter the Reynold's number and Reltive roughness:")
            sent=sent.split()
            for k in sent:
                k=str(k)
                if '.' in k:
                    k=list(k)
                    k=k.remove('.')
                    j=''
                    for o in k:
                        j+=o
                    if j.isdigit()==False:
                        sendMessage(chatid,"invalid number! please Enter again:")
                        break
                elif k.isdigit()==False:
                    sendMessage(chatid,"invalid number! please Enter again:")
                    break
                else:
                    m=1
            if m==1:
                Re=int(sent[0])
                ed=int(sent[1])
                h=fluids.friction.friction_factor(Re,ed)
                sendMessage(chatid,h)
        elif '/Reynold' in sent:
            sendMessage(chatid,"Enter the Density,velocity,diameter and viscosity:")
            sent=str(sent)
            sent=sent.split()
            m=0
            for b in sent:
                if '.' in b:
                    b=list(b)
                    b=b.remove('.')
                    j=''
                    for o in b:
                        j+=o
                    if j.isdigit()==False:
                        sendMessage(chatid,"invalid number! please Enter again:")
                        break
                elif b.isdigit()==False:
                    sendMessage(chatid,"invalid number! please Enter again:")
                    break
                else:
                    m=1
            if m==1:
                ro=int(sent[0])
                v=int(sent[1])
                d=int(sent[2])
                vis=int(sent[3])
                reynold=(ro*v*d)/vis
                sendMessage(chatid,reynold)         
        return Response('ok',status=200)
    else: 
        return ''

def write_json(data , filename = 'Reynolds.json'):
    with open(filename , 'w') as target:
        json.dump(data , target , indent=4 , ensure_ascii=False)

def read_json(filename = 'Reynolds.json'):
    with open(filename , 'r') as target:
        data = json.load(target)
    return data

write_json({})
app.run(host= "0.0.0.0" , port=int(os.environ.get('PORT' , 5000)))
