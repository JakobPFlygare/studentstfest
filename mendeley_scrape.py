# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:36:40 2019

@author: jflygare
"""

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import os

os.chdir('C:/Users/jflygare/Documents/ML_Projects/HackForSweden/')

from articles_prep import cleanText


master_source = requests.get('https://www.mendeley.com/research-papers/?query=global%20warming').content
#url = 'https://www.ncbi.nlm.nih.gov'

master_soup = BeautifulSoup(master_source,'lxml')
    
print(master_soup.prettify())

link = master_soup.find('div',class_='publication-details').a['href']
source = requests.get(link).content
soup = BeautifulSoup(source,'lxml')

#Tempfix
source = requests.get('https://www.mendeley.com/catalogue/climate-change-american-mind-2/').content
soup = BeautifulSoup(source,'lxml')

article = soup.find('div',id = 'root')

header = article.find('div',class_ = 'DocumentHeader__Info-sc-1v49xzf-2').h1.text

abstract = article.find('div',class_ = 'with-container body').p.text
print(abstract)



# Setting up csv files
csv_file = open('mendeley_scrape_ALL.csv','w',encoding="utf-8")

csv_writer = csv.writer(csv_file)   
csv_writer.writerow(['title','abstract'])



# LOOP THROUGH ALL

for i in range(1,6):
    pageLink = 'https://www.mendeley.com/research-papers/?query=climate%20change&page='+str(i)

    master_source = requests.get(pageLink).content
    master_soup = BeautifulSoup(master_source,'lxml')
    master_article = master_soup.find_all('div',class_='publication-details')
    
    for article in master_article:
        link = article.a['href']
        source = requests.get(link).content
        soup = BeautifulSoup(source,'lxml')
        
        
        page = soup.find('div',id = 'root')
        title = page.find('div',class_ = 'DocumentHeader__Info-sc-1v49xzf-2').h1.text
        abstract = page.find('div',class_ = 'with-container body').p.text
        
        cleanTitle = cleanText(title)
        cleanAbstract = cleanText(abstract)
        csv_writer.writerow([cleanTitle,cleanAbstract])
        
    
    
    
    
 
    
    
    

#OTHER FILE
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