from typing import Type
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import VotesParser




def votes(update: Update, context: CallbackContext):
    links = [
        "https://petition.president.gov.ua/petition/146960",
        "https://petition.president.gov.ua/petition/140908",
        "https://petition.president.gov.ua/petition/155356",
        "https://petition.president.gov.ua/petition/156774",
        "https://petition.president.gov.ua/petition/151810",
        "https://petition.president.gov.ua/petition/151938"

    ]
    messege = ""
    petitionsData =  VotesParser.processPetitionArr(links)
    for dataEl in petitionsData:
        messege += dataEl + "\n"
        messege += "--------------------------------------------------------------------"
        messege += "\n"
    
    #print(messege)
    
    
    update.message.reply_text(messege)


    



updater = Updater("5367058482:AAHB6YoooV46zM753Ng9UVJG3EyJpdTVT90",
                  use_context=True)
                  


updater.dispatcher.add_handler(CommandHandler('votes', votes))


updater.start_polling()
