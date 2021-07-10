url='https://api.telegram.org/bot1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w/'
import requests
import json
r={}
r['Reynolds']=[]
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

def text(x):
    return x['message']['text']

allmessage=getupdates()
lastmessage=getlast(allmessage)
chatid=chat_id(lastmessage)
sent=text(lastmessage)

if sent=="/start":
    send_message(chatid,"Hi {}! Enter your request:\n/Firiction_factor\n/Show\n/Help".format(lastmessage['message']['chat']['first_name']))
if sent=="/Firiction_factor":
    send_message(chatid,"Enter the Reynold's number:")
else:
    h=''
    if '.' in sent:
        w=list(sent)
        w.remove('.')
        for i in w:
            h+=i
        if h.isdigit()==False:  
            send_message(chatid,"invalid number! please Enter again:")
        else:
           r['Reynolds'].append(float(sent))
           send_message(chatid,"Enter the Relative roughness:")
    elif sent.isdigit()==False:
        send_message(chatid,"invalid number! please Enter again:")
    else:
        r['Reynolds'].append(float(sent))
        send_message(chatid,"Enter the Relative roughness:")