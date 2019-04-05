# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:36:40 2019

@author: jflygare
"""

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from articles_prep import cleanText

master_source = requests.get('https://www.ncbi.nlm.nih.gov/pubmed/?term=climate+change').content
url = 'https://www.ncbi.nlm.nih.gov'

master_soup = BeautifulSoup(master_source,'lxml')
    
print(master_soup.prettify())

master_article = master_soup.find('div')
print(master_article.prettify())


# Setting up csv files
csv_file = open('ncbi_scrape.csv','w',encoding="utf-8")

csv_writer = csv.writer(csv_file)   
csv_writer.writerow(['title','abstract'])

#Looping into all pages

for article in master_article.find_all('div',class_='rslt'):
    link = article.a['href']
    source = requests.get(url+link).content
    soup = BeautifulSoup(source,'lxml')
   
    article = soup.find('div',class_ = "rprt_all")
    
    title = article.h1.text
    cleanTitle = cleanText(title)
    abstract = article.find('div',class_ = 'rprt abstract').p.text
    cleanAbstract = cleanText(abstract)
    csv_writer.writerow([cleanTitle,cleanAbstract])
    
csv_file.close()


df = pd.read_csv('ncbi_scrape.csv',sep=",")