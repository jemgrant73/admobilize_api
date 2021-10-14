import requests as req
from requests.structures import CaseInsensitiveDict
import json

#variables

def getAccessToken(user, pw):
    endpoint = 'https://auth.admobilize.com/v2/accounts/-/sessions'
    headers = {'Content-type': 'application/json'}
    json = '{\"email\": \"' + user + '\", \"password\": \"' + pw + '\"}'
    token = req.post(endpoint, json, headers=headers).json()
    accessToken = token['accessToken']
    return accessToken

def getDeviceInfo(accessToken):
    endpoint = 'https://devicemanagementapi.admobilize.com/v2/projects/f6c95c34055114a298ec35219d37a0830/devices'
    headers = CaseInsensitiveDict()
    headers["Content-type"] = 'application/json'
    headers['Authorization'] = 'Bearer ' + accessToken
    response = req.get(endpoint, headers=headers)
    return response






# def getUserToken(idToken):
#     userToken = ''
#     return userToken


