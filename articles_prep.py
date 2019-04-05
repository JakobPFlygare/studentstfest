# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:34:12 2019

@author: jflygare
"""

# Import packages
import pandas as pd
import os
import numpy as np

os.chdir('C:/Users/jflygare/Documents/ML_projects/HackForSweden/')

#attempt 3

df = pd.read_table('articles.txt', delim_whitespace=False,header=None)
df.columns = ["abstract"]
    
new_df = pd.DataFrame({'abstract':df['abstract'].iloc[::2].values, 'keywords':df['abstract'].iloc[1::2].values})

import re

def cleanText (strDirty):
    clean = ''.join([i for i in strDirty if not i.isdigit()])
    clean = re.sub("[!@#$+%*:()'-?°‘’]", '', clean)
    clean = re.sub(' +',' ',clean)
    return clean

dfClean = new_df

for i in range(0,len(dfClean.index)):
    dfClean["abstract"][i] = cleanText(dfClean["abstract"][i])



