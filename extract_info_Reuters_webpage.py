# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:35:32 2020

@author: Moin Ahmed

This python script generates a csv file with global corona-related 
news from Reuters healine page
"""
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import csv
from datetime import datetime

myurl = 'https://www.reuters.com/news/archive/worldNews?date=today'
uClient = Request(myurl, headers={'User-Agent':'Mozilla/5.0'})
page_html = urlopen(uClient).read()

file = soup(page_html, 'html.parser')
    
stories = file.find_all('article',class_='story')

title, time_article, descrip, link=list(), list(), list(), list()
for i in range(len(file.find_all('article',class_='story'))-3):
    title.append(stories[i].h3.text.split('\t')[-1])
    time_article.append(stories[i].span.text)
    descrip.append(stories[i].p.text)
    link.append(stories[3].a['href'])
    
time_stamp = datetime.now()
    
csv_file = open('data_csv.csv','a')
csv_writer = csv.writer(csv_file)
for i in range(len(title)):
    csv_writer.writerow([title[i],time_article[i],time_stamp,descrip[i],link[i]])
csv_file.close()

