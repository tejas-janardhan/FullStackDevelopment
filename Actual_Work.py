import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

URL = 'https://www.monster.ca/jobs/search/?q=Software-Developer&where=canada&stpage=1&page=10'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
results = soup.find(id='SearchResults')

# print(results.prettify())

h_l = results.find_all('a')
df = []
for i in range(len(h_l)):
    page = requests.get(h_l[i]['href'])
    soup = BeautifulSoup(page.content, 'lxml')
    text = soup.get_text().split()
    df.append(pd.DataFrame(text, columns=['Words']))

df = pd.concat(df)

count = df['Words'].value_counts()
words_df = pd.read_csv('1-1000.txt', delimiter='\n', names=['Words'])

df = pd.DataFrame({'Words': count.index, 'Count': count.values})
df = df.loc[~df.Words.isin(words_df['Words']), :]
