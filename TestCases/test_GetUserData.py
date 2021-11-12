import requests
import json
import jsonpath
import pytest


@pytest.mark.Smoke
def test_fetch_user_details():
    url = "https://reqres.in/api/users"
    response = requests.get(url)

    # Parse response to json format
    json_response = json.loads(response.text)
    print(json_response)

    # Fetch value using Json path
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        print((first_name[0]))

