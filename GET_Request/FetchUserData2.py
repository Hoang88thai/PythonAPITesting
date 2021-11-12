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
jsonpath.jsonpath(json_response,'')
pages = jsonpath.jsonpath(json_response, 'total_pages')
# print(pages[0])
assert pages[0] == 2