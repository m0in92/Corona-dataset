# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:14:28 2020

@author: Moin Ahmed
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import csv
import numpy as np
import pandas as pd
from datetime import datetime
from name_clean import name_clean

with open('webpage3.html') as html_file:
    file = soup(html_file,"lxml")
    
name, t_cases, n_cases, t_deaths, n_deaths, t_recovered, active_cases, serious_condition, n_test, continent=list(),list(), list(), list(), list(),list(),list(),list(),list(),list()

time_date_now = datetime.now()
last_updated_on_website = file.find('div',class_='content-inner').find_all('div')[1].text.split(': ')[1]
for i in range(len(list(file.tbody.find_all('tr',class_ ='odd')))):
    name.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[1].text)
    t_cases.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[3].text)
    n_cases.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[5].text)
    t_deaths.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[7].text)
    n_deaths.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[9].text)
    t_recovered.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[11].text)
    active_cases.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[13].text)
    serious_condition.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[15].text)
    n_test.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[-6].text)
    continent.append(list(file.table.tbody.find_all('tr',class_ ='odd')[i])[-2].text)
    
for i in range(len(list(file.table.tbody.find_all('tr',class_ ='even')))):
    name.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[1].text)
    t_cases.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[3].text)
    n_cases.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[5].text)
    t_deaths.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[7].text)
    n_deaths.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[9].text)
    t_recovered.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[11].text)
    active_cases.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[13].text)
    serious_condition.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[15].text)
    n_test.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[-6].text)
    continent.append(list(file.table.tbody.find_all('tr',class_ ='even')[i])[-2].text)
    
name_clean(name)

# df = pd.DataFrame(np.array([t_cases, n_cases, t_deaths, n_deaths, t_recovered, active_cases,serious_condition, n_test, continent]).transpose(),index=name,columns=['t_cases, n_cases, t_deaths, n_deaths, t_recovered, active_cases, serious_condition, n_test, Continent'.split(',')])
# df['time_stamp'] = time_date_now
# df['last_updated_on_webpage']=last_updated_on_website

    

csv_file = open('data_csv.csv','a')
csv_writer = csv.writer(csv_file)
for i in range(len(name)):
    csv_writer.writerow([name[i],t_cases[i], n_cases[i], t_deaths[i], n_deaths[i], t_recovered[i], active_cases[i],serious_condition[i], n_test[i], continent[i], last_updated_on_website, time_date_now])
csv_file.close()



