import requests
import json
import jsonpath
import pytest

# API url
url = " https://reqres.in/api/users"


@pytest.mark.Smoke
def test_create_new_user():
    # Read Input Json File
    file = open("C:\\RMB\\QA\\Automation Courses\\CreateUser.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201


@pytest.mark.Sanity
def test_create_other_user():
    # Read Input Json File
    file = open("C:\\RMB\\QA\\Automation Courses\\CreateUser.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
