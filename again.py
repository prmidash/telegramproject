import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def start(update : Update , callback : CallbackContext):
    update.message.reply_text("Hi! Please Enter your request:\n/Friction_factor\n/Show\n/Help")

def Friction_factor(update : Update , callback : CallbackContext):
    update.message.reply_text("Please Enter Reynolds number")
def get_Reynolds(update : Update , callback : CallbackContext):
    Reynolds = update.message
    update.message.reply_text("Please Enter relative roughness")
def relative_roughness(update : Update , callback : CallbackContext):
    roughness = update.message






def main():
    updater = Updater("1882082108:AAFyoRnZucW21ffK1Y3H-uTwwIO50xLXd-g")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start" , start))
    dispatcher.add_handler(CommandHandler("Friction_factor" , Friction_factor))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command , get_Reynolds))
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