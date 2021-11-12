import requests
import json
import jsonpath

def test_oauth_api():
    Token_url="http://thetestingworldapi.com/Token"
    # Dictionary
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'adminpass'}
    response = requests.post(Token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization': 'Bearer '+token_value[0]}
    #print(response.text)

    API_URL = 'http://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(API_URL, headers=auth)
    print(response.text)