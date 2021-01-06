from bs4 import BeautifulSoup
import requests
from lxml import html

reqstring = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=web+developer&locT=&locId=&jobType=&context=Jobs&sc.keyword=web+developer&dropdown=0'
html_text = requests.get(reqstring).text
soup = BeautifulSoup(html_text, 'lxml')
print(soup)
