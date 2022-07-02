from typing import Type
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import VotesParser




def votes(update: Update, context: CallbackContext):
    votesStr = VotesParser.processData("https://petition.president.gov.ua/petition/146960",
    ".petition_votes_txt",
    ".petition_votes_txt > span"
    )
    mens = int(votesStr)
    votesStr = VotesParser.processData("https://petition.president.gov.ua/petition/140908",
    ".petition_votes_txt",
    ".petition_votes_txt > span"
    )
    students = int(votesStr)
    massage = "votes now: \n" + "age 18 - 60: " + str(mens) + "\nstudents: " + str(students)
    update.message.reply_text(massage)

def pagePetitionStat(update: Update, context: CallbackContext):
    votesStr = VotesParser.processData("https://petition.president.gov.ua/?status=active&sort=votes&order=desc",
    ".pet_title",
    ".pet_link"
    )
    print(Type(votesStr))
  
    #students = int(votesStr)
    #massage = "votes now: \n" + "age 18 - 60: " + str(mens) + "\nstudents: " + str(students)
    #update.message.reply_text(massage)
    



updater = Updater("5367058482:AAHB6YoooV46zM753Ng9UVJG3EyJpdTVT90",
                  use_context=True)
                  


updater.dispatcher.add_handler(CommandHandler('votes', votes))
updater.dispatcher.add_handler(CommandHandler('stat', pagePetitionStat))

updater.start_polling()
