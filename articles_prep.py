# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:34:12 2019

@author: jflygare
"""

# Import Pandas
import pandas as pd
import os
import numpy as np

os.chdir('C:/Users/jflygare/Documents/ML_projects/HackForSweden/')

article = pd.read_csv('article1.csv', sep='|',encoding='latin-1')



import csv

csv.register_dialect('myDialect',
delimiter = '\t',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)

with open('article1.csv', 'r') as f:
    reader = csv.reader(f, dialect='myDialect')
    for row in f:
        print(row[2])
        
print(row["Value"])



#attempt 3

df = pd.read_table('articles.txt', delim_whitespace=False,header=None)
df.columns = ["text"]
    
h = df[1::2].assign(start=df[::2].index)
h = df.loc[df.text.eq(2)].assign(start=df.loc[df.text.eq(1)].index)

new_df = pd.DataFrame({'text':df['text'].iloc[::2].values, 'keywords':df['text'].iloc[1::2].values})


import re


def cleanText (strDirty):
    clean = ''.join([i for i in strDirty if not i.isdigit()])
    clean = re.sub("[!@#$+%*:()'-?°‘’]", '', clean)
    clean = re.sub(' +',' ',clean)
    return clean


dfClean = df

for i in dfClean["text"]:
    dfClean["text"] = cleanText(i)


