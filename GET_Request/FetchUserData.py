# To make a request to the server and get response from the server.
# We are going to use a request module so I'm saying  import request.

import requests


# API URL
url = "https://reqres.in/api/users?page=2" # put it in double quote because it is string

# send Get request
response = requests.get(url)
# print(response)

# Display response content
# print(response.content)
print(response.headers)