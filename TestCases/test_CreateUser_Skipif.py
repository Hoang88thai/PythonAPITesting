import requests
import json
import jsonpath
import pytest

# API rul
url = "https://reqres.in/api/users?page=2"
a = 100


# @pytest.mark.skipif(a>10,reason="Condition is not satisfy")
def test_create_new_user():
    # Read Input Json File
    file = open("C:\\RMB\\QA\\Automation Courses\\CreateUser.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201


def test_create_other_user():
    # Read Input Json File
    file = open("C:\\RMB\\QA\\Automation Courses\\CreateUser.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
