import pandas as pd
import requests
from bs4 import BeautifulSoup


def scraper(search_term):
    URL = f'https://www.monster.ca/jobs/search?q={search_term}&where=canada'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')

    job_elems = results.find_all('section', class_='card-content')

    results_df = pd.DataFrame(columns=['Title', 'Company', 'Location'])

    for job_elem in job_elems:

        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')

        results_df = results_df.append(pd.DataFrame([title_elem.text.strip(), company_elem.text.strip(), location_elem.text.strip()], columns=['Title', 'Company', 'Location']), ignore_index=True)

    return results_df



scraper('IT')