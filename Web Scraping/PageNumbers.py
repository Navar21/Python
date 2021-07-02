# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:06:49 2021

@author: mrbar
"""

import requests

from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Premier_League"

data = requests.get(url)

soup = BeautifulSoup(data.content, 'html.parser')
    
results = soup.find_all(class_ = 'navbox-list navbox-odd')[0]

x = results.find_all('span', class_ = 'nowrap')

season = [title.get('title') for ul in x for title in ul.findAll('a')]

list_of_seasons = []
for title in range(len(season)):
    list_of_seasons.append(season[title].replace(" ", "_"))