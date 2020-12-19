from bs4 import BeautifulSoup
import requests
import lxml

import urllib
import httplib2

# url = 'https://adfs.uwaterloo.ca/adfs/ls/?client-request-id=ee2d7ff9-a639-4ffa-f302-00800210003b'
url = 'https://waterlooworks.uwaterloo.ca/myAccount/dashboard.htm'
headers = {'Content-type': 'application/x-www-form-urlencoded', 'Cookie': {'BIGipServerCECA_443.app~CECA_443_pool':
                                                                           'rd2o00000000000000000000ffffac108932o23111', 'JSESSIONID': '3FF5EC3E229CC54EF8819DB52F2A17B7'}}
# headers['BIGipServerCECA_443.app~CECA_443_pool'] = 'rd2o00000000000000000000ffffac108932o23111'
# headers['JSESSIONID'] = '3FF5EC3E229CC54EF8819DB52F2A17B7'
print(headers)
http = httplib2.Http()
response, content = http.request(
    url, 'GET', headers=headers)

# print(response)
# soup = BeautifulSoup(html_text, 'lxml')

# print(soup.prettify())
