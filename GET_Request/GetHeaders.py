import requests

headerdata ={'T1':'First_Header','T2':'Second_Header'}

respone  = requests.get('https://httpbin.org/get', headers = headerdata)
print(respone.text)