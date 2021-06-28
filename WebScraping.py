# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:19:49 2021

@author: mrbar
"""

import requests
from bs4 import BeautifulSoup
from PageNumbers import list_of_seasons

for index in range(len(list_of_seasons) - 1):
    url = "https://en.wikipedia.org/wiki/{}".format(list_of_seasons[index])

    data = requests.get(url)

    soup = BeautifulSoup(data.content, 'html.parser')
    
    if index == 27:
        results = soup.find_all('table', class_ = 'wikitable')[3]
    else:
        results = soup.find_all('table', class_ = 'wikitable')[3]
    '''
    This part obtains the position of the clubs in the table as well as
    the names of the clubs participating in that season
    '''
    tr = [position.text.strip() for position in results.find_all('tr')]
    position = [number for number in range(1, len(tr))]
    
    club = [club.text.strip() for club in results.find_all('th')[11:]] 
    x = list(zip(position, club))

    with open('{}.txt'.format(list_of_seasons[index]), 'w+') as f:
        for i in range(len(x)):
            f.write(str(x[i]))
            f.write('')