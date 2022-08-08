import string
import time
from tokenize import Number
from turtle import update
import requests
from bs4 import BeautifulSoup as BS

def getPetitionsPage(requestURL):
    petitionPage = requests.get(requestURL)
    
    html = BS(petitionPage.content, 'html.parser')
    
    pName = html.select(".pet_number + h1").pop().text
    pStatus = html.select(".petition_votes_status").pop().text
    pVotes = html.select(".petition_votes_txt > span").pop().text
    pLink = str(requestURL)
    messege = "Name: " + pName + "\n" + pStatus + "\n votes: " + pVotes + "\n link: " + pLink
        
    return messege





def processPetitionArr(petitinoArr = []):
    petitionsData =[]
    for petitionLink in petitinoArr:
        petitionPage = getPetitionsPage(petitionLink)
        petitionsData.append(petitionPage)
    return petitionsData


