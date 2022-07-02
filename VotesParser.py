import time
from tokenize import Number
from turtle import update
import requests
from bs4 import BeautifulSoup as BS

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
