from bs4 import BeautifulSoup
import requests
import lxml

import urllib
import json
import httplib2

# url = 'https://adfs.uwaterloo.ca/adfs/ls/?client-request-id=ee2d7ff9-a639-4ffa-f302-00800210003b'
url = 'https://adfs.uwaterloo.ca/adfs/ls/'
body = {'UserName': 'jbalamur@uwaterloo.ca', 'Password': 'nuhnesW-1102'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}

http = httplib2.Http()
response, content = http.request(
    url, 'POST', headers=headers, body=urllib.parse.urlencode(body))

print(response)
# print(conten)

# headers = {'Cookie': response['set-cookie']}
