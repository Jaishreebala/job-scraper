from bs4 import BeautifulSoup
import requests
from lxml import html

field = "web"
location = "Waterloo%2C%2BOntario%2C%2BCanada"
pageNo = 0
reqstring = f'https://www.linkedin.com/jobs/search?keywords={field}&location={location}&trk=homepage-jobseeker_jobs-search-bar_search-submit&currentJobId=2342605609&position=2&pageNum={pageNo}'
html_text = requests.get(reqstring).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all(
    'li', class_="result-card job-result-card result-card--with-hover-state")

for job in jobs:
    link = job.find('a', class_="result-card__full-card-link")
    jobTitle = job.find(
        'h3', class_="result-card__title job-result-card__title").text
    employer = job.find(
        'a', class_="result-card__subtitle-link job-result-card__subtitle-link").text
    print(f"""
    Link: {link.get('href')}\n
    Job Tile: {jobTitle}\n 
    Employer: {employer}
    """)
