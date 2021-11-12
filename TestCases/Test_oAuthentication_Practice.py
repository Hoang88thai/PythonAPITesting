import requests
import json
import jsonpath

def test_oAuth_api():
    token_URL = "http://thetestingworldapi.com/Token"
    # create a dictionary to
    data ={'grant_type': 'password', 'username': 'admin', 'password':'adminpass'}
    response = requests.post(token_URL, data)
    #Fetch token value from access_token
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    #So whatever the data we got as authorization token it will be a list I want to fech 0 index value of this list
    # and I want to set it as an authorization..
    auth = {'authorization': 'Bearer '+ token_value[0]}
    API_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(API_URL, headers=auth)
    print(response.text)
