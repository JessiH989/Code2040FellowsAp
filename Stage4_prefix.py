#Jessi Hernandez
#Code2040 Fellows Application // Prefix
#Stage 4

import requests
import json

def STAGE4_prefix():

    API_token = 'c3ef305c42d60f1ef3eda0527c743cb2'
    PREFIX_url = 'http://challenge.code2040.org/api/prefix'

    req = requests.post(PREFIX_url, data = {'token': API_token})

    #Create JSON dictionary
    dict = req.json()

    #Pulling out the prefix and array from dictionary
    prefix = dict['prefix']
    array = dict['array']

    result = []

    #Returning an array containing only the strings that do not start with that prefix
    ARRAY_result = [A for A in array if A[0:len(prefix)] != prefix]
    
    VALIDATE_url = 'http://challenge.code2040.org/api/prefix/validate'
    
    r = requests.post(VALIDATE_url, json = {'token':API_token, 'array':ARRAY_result})

STAGE4_prefix()
