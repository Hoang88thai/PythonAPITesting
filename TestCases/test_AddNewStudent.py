import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/hthai/Desktop/Task_API/RequestJson.json', 'r')

    # Parse (transform) into json format. I want to read the content of the file
    # then transform it into the form of json
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/526232"
    response =requests.get(API_URL)
    # whatever response, we translating into json format, typecasting json format
    json_response = json.loads(response.text)
    # Apply json path
    id = jsonpath.jsonpath(json_response,'data.id')
    # assert  id(0) == 526231

def test_update_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/526232"
    f = open('C:/Users/hthai/Desktop/Task_API/RequestJson_Update.json', 'r')

    # Parse (transform) into json format. I want to read the content of the file
    # then transform it into the form of json
    json_request = json.loads(f.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/526232"
    response =requests.get(API_URL)
    # whatever response, we translating into json format, typecasting json format
    json_response = json.loads(response.text)
    # json_response = response.json()
    print(json_response)
    # Apply json path
    id = jsonpath.jsonpath(json_response,'data.id')
    # assert  id(0) == 526231

def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/526232"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/526232"
    response = requests.get(API_URL)
    # whatever response, we translating into json format, typecasting json format
    json_response = json.loads(response.text)
    # json_response = response.json()
    print(json_response)
    # Apply json path
    id = jsonpath.jsonpath(json_response, 'data.id')
    # assert  id(0) == 526231
