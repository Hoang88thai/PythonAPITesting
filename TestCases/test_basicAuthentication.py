import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('hoang88thai@gmail.com', 'HTocean12QWg'))
    print(response.text)