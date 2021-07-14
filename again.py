import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
import fluids
import os

m=0
def start(update : Update , callback : CallbackContext):
    update.message.reply_text("Hi {}! Please Enter your request:\n/Friction_factor\n/Reynolds".format(update.message.from_user.first_name))
def Friction_factor(update : Update , callback : CallbackContext):
    update.message.reply_text("Please enter Reynolds number and Relative roughness like:\nR number,E number")
def Reynold(update : Update , callback : CallbackContext):
    update.message.reply_text("Please enter Density, Diameter, Velocity and Viscosity like:\nD num,d num,v num,vis num")
def F(update : Update , callback : CallbackContext):
    s=str(update.message.text)
    s=s.split(',')
    if len(s)==2:
        R=s[0]
        E=s[1]
        R=R.split()
        E=E.split()
        if R[0]=='R' and E[0]=='E':
            if '.' in R[1]:
                q=R[1]
                R[1]=list(R[1])
                R[1].remove('.')
                e=''
                for o in R[1]:
                    e+=o
                if e.isdigit()==False:
                    update.message.reply_text("Invalid number! Please enter again")
                else:
                    q = float(q)
                    Reynolds=q
            elif R[1].isdigit()==False:
                update.message.reply_text("Invalid number! Please enter again")
            else:
                R[1] = float(R[1])
                Reynolds=R[1]
                if '.' in E[1]:
                    w=E[1]
                    E[1]=list(E[1])
                    E[1].remove('.')
                    e=''
                    for o in E[1]:
                        e+=o
                    if e.isdigit()==False:
                        update.message.reply_text("invalid number! please enter again:")
                    else:
                       w=float(w)
                       roughness=w
                       f=fluids.friction.friction_factor(Reynolds,roughness)
                       update.message.reply_text(f) 
                elif E[1].isdigit()==False:
                    update.message.reply_text("invalid number! please enter again:")
                else:
                    E[1]=float(E[1])
                    roughness=E[1]
                    f=fluids.friction.friction_factor(Reynolds,roughness)
                    update.message.reply_text(f)
                    
    else:
        r={}
        for a in s:
            a=a.split()
            r[a[0]]=float(a[1])
        re=((r['D'])*(r['d'])*(r['v']))/(r['vis'])  
        update.message.reply_text(re)
        
def main():
    updater = Updater("1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start" , start))
    dispatcher.add_handler(CommandHandler("Friction_factor" , Friction_factor))
    dispatcher.add_handler(CommandHandler("Reynolds" , Reynold))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,F))
    updater.start_webhook(listen="0.0.0.0",port=int(os.environ.get('PORT' , 5000)),TOKEN="1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w",url="https://fluid-mechanic.herokuapp.com/1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w")
    updater.idle()

if __name__ == "__main__":
    main() 


"""def play(update : Update , callback : CallbackContext):
    if not update.message.text.isdigit():
        update.message.reply_text("Enter a number")
        return
    num = update.message.from_user.id%1000 + 1
    inputnum = int(update.message.text)
    if inputnum>num:
        update.message.reply_text("Enter a lower number")
    if inputnum<num:
        update.message.reply_text("Enter a higher number")
    if inputnum==num:
        update.message.reply_text("you won!")"""
