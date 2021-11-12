import requests

# API URL
url = "https://reqres.in/api/users?page=2"

#send GET Request
response = requests.get(url)

# Validate Status Code
print(response.status_code)

assert response.status_code == 200

# Fetch Response header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)

# Fetch Elapse time
print(response.elapsed)