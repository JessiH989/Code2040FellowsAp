#Jessi Hernandez
#Code2040 Fellows Application // Registration
#Stage 1

import requests

def STAGE1_registration():

  MYGITHUB_url = 'https://github.com/JessiH989/Code2040FellowsAp' 
  REGISTRATION_endpoint = 'http://challenge.code2040.org/api/register'
  API_token = 'c3ef305c42d60f1ef3eda0527c743cb2'

  #JSON Dictionary
  JSON_token = {'github': MYGITHUB_url, 'token': API_token}

  #Connecting MYGITHUB_url to the REGISTRATION_endpoint with my API_token
  r = requests.post(REGISTRATION_endpoint, JSON_token)

STAGE1_registration()
