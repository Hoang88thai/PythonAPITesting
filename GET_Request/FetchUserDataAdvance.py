import requests
import json
import jsonpath


url = "https://reqres.in/api/users?page=2"
response = requests.get(url)  # getting this response and stored in the response object

# print(response.content)

# parse response to Json format
json_response = json.loads(response.text)
# print(json_response)

# Fetch value using Json Path
for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+ str(i) + '].first_name')
    print((first_name[0]))



