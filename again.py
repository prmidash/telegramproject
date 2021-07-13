import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
import fluids
r={}

def start(update : Update , callback : CallbackContext):
    update.message.reply_text("Hi! Please Enter your request:\n/Friction_factor\n/Reynolds\n/Help")

def Friction_factor(update : Update , callback : CallbackContext):
    update.message.reply_text("Please Enter Reynold's number:")
    s=str(update.message)
    if '.' in s:
        s=s.split()
        s.remove('.')
        e=''
        for o in s:
            e+=o
        if e.isdigit()==False:
            update.message.reply_text("invalid number! please enter again:")
    elif s.isdigit()==False:
        update.message.reply_text("invalid number! please enter again:")
    else:
        Reynolds = update.message
        update.message.reply_text("Please Enter relative roughness:")
        s=str(update.message)
        if '.' in s:
            s=s.split()
            s.remove('.')
            e=''
            for o in s:
                e+=o
            if e.isdigit()==False:
                update.message.reply_text("invalid number! please enter again:")
        elif s.isdigit()==False:
            update.message.reply_text("invalid number! please enter again:")
        else:
            roughness=update.message
            m=2
            if m==2:
                f=fluids.friction.friction_factor(Reynolds,roughness)
                update.message.reply_text(f)
def hi(update : Update , callback : CallbackContext):
    update.message.reply_text("hiii")

def main():
    updater = Updater("1716629236:AAF48G2vsOYNv_yPOJsUUAdajdtHInlQv0w")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start" , start))
    dispatcher.add_handler(CommandHandler("Friction_factor" , Friction_factor))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command , hi))
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
