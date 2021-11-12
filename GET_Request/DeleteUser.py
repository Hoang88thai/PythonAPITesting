import requests

url = "https://reqres.in/api/users/2"

response = requests.delete(url) # Response is 204 for delete

# fetch response code
# print(response.status_code)

assert response.status_code == 204