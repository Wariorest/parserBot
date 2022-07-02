import time
from tokenize import Number
from turtle import update
import requests
from bs4 import BeautifulSoup as BS

def getVotesNumber(requestURL, htmlSelectClass = "", elSelectClass = ""):
    r = requests.get(requestURL)
    html = BS(r.content, 'html.parser')
    for el in html.select(htmlSelectClass):
        votes = el.select(elSelectClass)
    return votes


def processData(requestURL, htmlSelectClass = "", elSelectClass = ""):
    votesNumber = getVotesNumber(requestURL, htmlSelectClass, elSelectClass)
    return(votesNumber.pop().text)


def votesPerHour(fVotesPoint, sVotesPoint):
    votesPerHour = fVotesPoint - sVotesPoint
    return votesPerHour


