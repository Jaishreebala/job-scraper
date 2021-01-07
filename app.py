from bs4 import BeautifulSoup
import requests
from lxml import html

field = input("Enter Field: ")
location = input("Enter Location [eg: Waterloo, Ontario, Canada]: ")
location = location.replace(",", "%2C")
skills = []
resultList = []
while True:
    skillInput = input("Enter Skill (type done when done): ")
    if(skillInput == "done"):
        break
    else:
        skills.append(skillInput)

print("Searching for jobs... Might take a minute, hang tight! :D")

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

        queryJobString = link.get('href')
        job_html = requests.get(queryJobString).text
        job_soup = BeautifulSoup(job_html, 'lxml')
        job_text = job_soup.find_all(
            'div', class_="show-more-less-html__markup show-more-less-html__markup--clamp-after-5")
        skillMatch = []
        for elem in job_text:
            for skill in skills:
                if(elem.text):
                    if skill.lower() in elem.text.lower():
                        skillMatch.append(skill)
        if(len(skillMatch) > 0):
            jobList = [jobTitle, employer,
                       round(len(skillMatch)/len(skills)*100, 2), skillMatch, link.get('href')]
            resultList.append(jobList)
            resultList.sort(key=lambda x: x[2], reverse=True)


for res in resultList:
    print(f"""
    Job Tile: {res[0]}\n
    Employer: {res[1]}\n
    % Match : {res[2]}%\n
    Skills  : {res[3]}\n
    Job Link: {res[4]}\n
    """)
