from bs4 import BeautifulSoup
import requests
from lxml import html

field = input("Enter Field: ")
location = input("Enter Location [eg: Waterloo, Ontario, Canada]: ")
location = location.replace(",", "%2C")
skills = []

while True:
    skillInput = input("Enter Skill (type done when done): ")
    if(skillInput == "done"):
        break
    else:
        skills.append(skillInput)

print(skills)

pageNo = 0
reqstring = f'https://www.linkedin.com/jobs/search?keywords={field}&location={location}&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=2&pageNum={pageNo}'
html_text = requests.get(reqstring).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all(
    'li', class_="result-card job-result-card result-card--with-hover-state")

if len(jobs) == 0:
    print("no results found")
else:
    for job in jobs:
        link = job.find('a', class_="result-card__full-card-link")
        jobTitle = job.find(
            'h3', class_="result-card__title job-result-card__title").text
        employer = job.find(
            'a', class_="result-card__subtitle-link job-result-card__subtitle-link")
        if (employer):
            employer = employer.text
        print(f"""
        Link: {link.get('href')}\n
        Job Tile: {jobTitle}\n
        Employer: {employer}
        """)
