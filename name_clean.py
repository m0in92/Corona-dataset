# -*- coding: utf-8 -*-
"""
This function removes unnessecary characters from the continents 
names. These characters are added during the web scrapping method.
 
Created on Tue Apr 14 21:17:10 2020

@author: Moin Ahmed
"""

def name_clean(name):
    for i in range(len(name)):
        if len(name[i].split('\n'))>1:
            name[i] = name[i].split('\n')[1]
    return name