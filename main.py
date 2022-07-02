from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import VotesParser





def start(update: Update, context: CallbackContext):
    votesStr = VotesParser.processData("https://petition.president.gov.ua/petition/146960")
    mens = int(votesStr)
    votesStr = VotesParser.processData("https://petition.president.gov.ua/petition/140908")
    students = int(votesStr)
    massage = "votes now: \n" + "age 18 - 60: " + str(mens) + "\nstudents: " + str(students)
    update.message.reply_text(massage)    
    
    



updater = Updater("5367058482:AAHB6YoooV46zM753Ng9UVJG3EyJpdTVT90",
                  use_context=True)
                  


updater.dispatcher.add_handler(CommandHandler('votes', start))

updater.start_polling()
