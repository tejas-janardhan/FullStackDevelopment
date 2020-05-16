import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.ca/jobs/search?q=information-technology&where=canada'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

# for job_elem in job_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#
#     if title_elem is not None:
#         print(title_elem.text.strip())
#
#     if company_elem is not None:
#         print(company_elem.text.strip())
#
#     if title_elem is not None:
#         print(title_elem.text.strip())
#         print('\n')

# python_jobs = results.find_all('h2', string='Pyhton Developer')

python_jobs = results.find_all('h2', string=lambda text: 'pyhton' in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
