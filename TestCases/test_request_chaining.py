import requests
import json
import jsonpath

def test_add_new_student():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/hthai/Desktop/Task_API/AddStudent.json', 'r')
    # read the content and parse into json format
    json_request = json.loads(f.read())
    # Create a new account
    response = requests.post(API_URL, json_request)
    # Fetch the response
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])
    # print(response.text)

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(API_URL)
    print(response.text)
