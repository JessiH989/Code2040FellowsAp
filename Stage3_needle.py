#Jessi Hernandez
#Code2040 Fellows Application // Needle In A Haystack
#Stage 3

import requests
import json

def STAGE3_needle():
    API_token = 'c3ef305c42d60f1ef3eda0527c743cb2'
    ENDPOINT_url = 'http://challenge.code2040.org/api/haystack'
    VALIDATE_url = 'http://challenge.code2040.org/api/haystack/validate'

    r = requests.post(ENDPOINT_url, data = {'token': API_token})
    
    dict = r.json()
    #Remove both NEEDLE and HAYSTACK from the JSON dictionary
    needle = dict['needle']
    haystack = dict['haystack']

    #Pulling out the NEEDLE from the "HAYSTACK"
    index = haystack.index(needle)

    r = requests.post(VALIDATE_url, data = {'token':API_token, 'needle': index})

STAGE3_needle() 
