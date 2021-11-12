import requests
import json
import jsonpath

url = " https://reqres.in/api/users?page=2"

# read json file  -- double back flash for file handling
file = open("C:\\RMB\\QA\\Automation Courses\\UpdatedData.json", 'r')  # open in read mode 'r'

# call read method to read complete content and store into json_input variable
json_input = file.read()

# This file.read() content is simply a string. I want type casting. I  want to parse this file into the form of Json
# So you're using Json.loads which is going to parse this data into Json format. So that's request_json which you've created.
# parse data (json_input) into json with using json.loads
request_json = json.loads(json_input)

# print(request_json)

# make a put request with json input body.
# requests.put will give a response which will be stored in the response object
response = requests.put(url,request_json)
# print(response.content)

# assert response.status_code == 200

# Fetch header from response

print(response.headers.get('Content-length'))

# Response we're getting now is in the form of string, if you want to use it, you need to parse it into json format
# Parse response into json format. This a typecasting
response_json = json.loads(response.text)

# Fetch value using json Path
# pick Id using json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])