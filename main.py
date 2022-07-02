import time
from tokenize import Number
from turtle import update
import requests
from bs4 import BeautifulSoup as BS


from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


def getVotesNumber(requestURL):
    r = requests.get(requestURL)
    html = BS(r.content, 'html.parser')

    for el in html.select(".petition_votes_txt"):
        votes = el.select('.petition_votes_txt > span')

    return votes


def processData(requestURL):
    votesNumber = getVotesNumber(requestURL)
    return(votesNumber.pop().text)


def votesPerHour(fVotesPoint, sVotesPoint):
    votesPerHour = fVotesPoint - sVotesPoint
    return votesPerHour


def start(update: Update, context: CallbackContext):
    mens = int(processData("https://petition.president.gov.ua/petition/146960"))
    students = int(processData("https://petition.president.gov.ua/petition/140908"))
    massage = "votes now: \n" + "age 18 - 60: " + str(mens) + "\nstudents: " + str(students)
    update.message.reply_text(massage)    
    
    



updater = Updater("5367058482:AAHB6YoooV46zM753Ng9UVJG3EyJpdTVT90",
                  use_context=True)
                  


updater.dispatcher.add_handler(CommandHandler('votes', start))

updater.start_polling()
