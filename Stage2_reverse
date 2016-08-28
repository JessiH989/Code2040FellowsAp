#Jessi Hernandez
#Code2040 Fellows Application // Reverse A String
#Stage 2

import requests

def STAGE2_reverse():
    
    API_token = 'c3ef305c42d60f1ef3eda0527c743cb2'
    REVERSE_url = 'http://challenge.code2040.org/api/reverse'
    
    r = requests.post(REVERSE_url, data = {'token': API_token})
    reversed = r.text[::-1]
    
    VALIDATE_url = 'http://challenge.code2040.org/api/reverse/validate'
    r = requests.post(VALIDATE_url, data = {'token': API_token, 'string': reversed})

STAGE2_reverse()
