import requests
from bs4 import BeautifulSoup

import pandas as pd

URL = "https://www.euro-millions.com/pt/arquivo-de-resultados-"
rqst = requests.get(URL + "2022")
soup = BeautifulSoup(rqst.content, 'html5lib')
#print(soup)

years_html = soup.find('ul', attrs={'class': 'year'})
years_list = []
for row in years_html.find_all('a'):
    years_list.append(row.text)

print('Years to process: ', years_list)

json = {}
balls_list = []
stars_list = []
results_html = soup.find_all('ul', attrs={'class': 'balls small'})
print('Number of results: ', str(len(results_html)))
for result in results_html:
    for row in result.find_all('li', attrs={'class': 'new ball'}):
        balls_list.append(row.text)
    for row in result.find_all('li', attrs={'class': 'new lucky-star'}):
        stars_list.append(row.text)
print(balls_list)
print(stars_list)
#content = driver.page_source
#soup = BeautifulSoup(content)
#print(soup)
#years = driver.find_element()
#results_year_list = []

#for i in range(years):
#    results_year_list.append(years[i].text)
#
#print(results_year_list)

