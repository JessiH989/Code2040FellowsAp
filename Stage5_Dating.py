#Jessi Hernandez
#Code2040 Fellows Application // Dating
#Stage 5

import requests, datetime, time
from datetime import timedelta

def STAGE5_dating():

    API_token = 'c3ef305c42d60f1ef3eda0527c743cb2'
    DATING_endpoint = 'http://challenge.code2040.org/api/dating'
    
    req = requests.post(DATING_endpoint, data = {'token': API_token})

    #Create JSON dictionary
    dict = req.json()

    #Pulling out the datestamp and interval from dictionary
    datestamp = dict['datestamp']
    interval = dict['interval']
    
    #Converted string to date object
    DATESTAMP_obj = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
    
    #Add interval to date
    TIME_interval = DATESTAMP_obj + datetime.timedelta(seconds = interval)
    
    #Converting to iso string with added interval to date
    DATE_final = (DATESTAMP_obj + timedelta(seconds = interval)).isoformat() + 'Z'
    
    VALIDATE_results = 'http://challenge.code2040.org/api/dating/validate'
    
    r = requests.post(VALIDATE_results, data = {'token':API_token, 'datestamp':DATE_final})

STAGE5_dating()
