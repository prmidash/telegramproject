import logging
from telegram import Update, message, user
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, dispatcher
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update:Update, callback:CallbackContext):
    update.message.reply_text("matni ke mikhaym bot dar javab start type konad")   #dastoor chap baray bot
    pass

def play(up:Update, callback:CallbackContext):
    #update.message.text-> matn payam frestade shode ke string ast
    #update.message.reply_text("")->dastoor chap
    #update.message.from_user.id-> id fard ferestande payam ra midahad(be jay id mitavand etelaat digar fard bashad)
    pass

def main():
    updater=Updater("token")
    dispatcher=updater.dispatcher                                                 #nahve barkhord bot ba payamha
    dispatcher.add_handler(CommandHandler("start",start))                         ##barkhord bot ba command ha->tabe start neveshte shode
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,play))  ## barkhord bot ba sayer payamha( az & baray 'and' va az ~ baray 'not' estefade mishavad)
    updater.start_polling()            #shoro daryaft payamha (az webhook ham mishe)
    updater.idle()                     #baray kharej kardan bot ya barname az run. (ba ctrl+c)

if __name__=="__main__":
    main()