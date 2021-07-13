import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
import fluids

m=0
def start(update : Update , callback : CallbackContext):
    update.message.reply_text("Hi {}! Please Enter your request:\n/Friction_factor\n/Reynolds\n/Help".format(update.message.from_user.first_name))

def Friction_factor(update : Update , callback : CallbackContext):
    update.message.reply_text("Please Enter Reynold's and Relative roughness number like:\nR number,E number")
def Reynold(update : Update , callback : CallbackContext):
    update.message.reply_text("please enter Density, Diameter, Velocity and Viscosity like:\nD num,d num,v num,vis num")
def F(update : Update , callback : CallbackContext):
    s=str(update.message.from_user)
    s=s.split(',')
    if len(s)==2:
        R=s[0]
        E=s[1]
        R=R.split()
        E=E.split()
        if R[0]=='R' and E[0]=='E':
            if '.' in R[1]:
            R[1]=list(R[1])
            R[1].remove('.')
            e=''
            for o in s:
                    e+=o
            if e.isdigit()==False:
                update.message.reply_text("invalid number! please enter again:")
            elif R[1].isdigit()==False:
                update.message.reply_text("invalid number! please enter again:")
            else:
                Reynolds = int(R[1])
                if '.' in E[1]:
                    E[1]=list(E[1])
                    E[1].remove('.')
                    e=''
                    for o in s:
                        e+=o
                    if e.isdigit()==False:
                        update.message.reply_text("invalid number! please enter again:")
                elif s.isdigit()==False:
                    update.message.reply_text("invalid number! please enter again:")
                else:
                    roughness=int(s[1])
                    f=fluids.friction.friction_factor(Reynolds,roughness)
                    update.message.reply_text(f)
    else:
        r={}
        for a in s:
            a=a.split()
            r[a[0]]=int(a[1])
        re=((r['D'])*(r['d'])*(r['v']))/(r['vis'])  
        update.message.reply_text(re)
def main():
    updater = Updater("1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start" , start))
    dispatcher.add_handler(CommandHandler("Friction_factor" , Friction_factor))
    dispatcher.add_handler(CommandHandler("Reynolds" , Reynold))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,F))
    updater.start_polling()
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
