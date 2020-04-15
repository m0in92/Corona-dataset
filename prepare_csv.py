# -*- coding: utf-8 -*-
"""
This script will create column headings in the data_csv file.

Created on Tue Apr 14 18:47:37 2020

@author: Moin Ahmed
"""

import csv

csv_file = open('data_csv.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','t_cases', 'n_cases', 't_deaths', 'n_deaths'
                     , 't_recovered', 'active_cases', 'serious_condition', 
                     'n_test', 'Continent', 'last_updated_on_website', 'time_date_now'])

csv_file.close()