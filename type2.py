# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:17:41 2021

@author: aksha
"""

from pywebio.input import *
from pywebio.output import *
import numpy as np
import pandas as pd

df_first=pd.read_csv('tmdb_5000_movies.csv')
df_second=pd.read_csv('movies.csv')
df_third=pd.read_csv('ratings.csv')

put_text("SUGGESTING MOVIES BASED ON CONTENT PREVIOUSLY WATCHED AND ALSO PREDICT THE RATING FOR THE NEW MOVIES BASED ON THE USER")

data = input_group("Input Movies and their corresponding ratings",[
  
  textarea('Text Area', rows=3, placeholder='Some text',name='name'),
    textarea('Rating Area', rows=3, placeholder='Some text',name='rate')
])

title_new=list()
for index,row in df_second.iterrows():
    x=row['title']
    try:
        i=x.index('(')
    except:
        continue
    title_new.append(row['title'][:i])
title_new=pd.DataFrame(title_new)  
df_second.drop(['title'],axis=1,inplace=True)
title_new.columns=['title']
df_second=pd.concat([df_second,title_new],axis=1)
df_second['genres']=df_second.genres.str.split('|')
df=df_second.iloc[:5,:]

names=data['name'].split('\n')
rating=[int(i) for i in data['rate'].split('\n')]
rating=np.array(rating)

Comedy=list()
Drama=list()
Romance=list()
for index,row in df_second.iterrows():
    if 'Comedy' in row['genres']:
        Comedy.append(1)
    else:
        Comedy.append(0)
    if 'Drama' in row['genres']:
        Drama.append(1)
    else:
        Drama.append(0)
    if 'Romance' in row['genres']:
        Romance.append(1)
    else:
        Romance.append(0)

        
df_second=pd.concat([df_second,pd.DataFrame(Comedy,columns=['Comedy'])],axis=1)
df_second=pd.concat([df_second,pd.DataFrame(Drama,columns=['Drama'])],axis=1)
df_second=pd.concat([df_second,pd.DataFrame(Romance,columns=['Romance'])],axis=1)    

df_calc=df_second[['genres','title','Comedy','Drama','Romance']]
df_calc=df_calc.iloc[2:5,:]
df_calc=df_calc[['Comedy','Drama','Romance']]

df_calc=df_calc.mul(rating,axis=0)
user_profile=list()
user_profile.append(df_calc['Comedy'].sum())
user_profile.append(df_calc['Drama'].sum())
user_profile.append(df_calc['Romance'].sum())

df_second['Comedy']=df_second['Comedy']*user_profile[0]
df_second['Drama']=df_second['Drama']*user_profile[1]
df_second['Romance']=df_second['Romance']*user_profile[2]
df_second['score']=df_second['Comedy']+df_second['Romance']+df_second['Drama']
df_second.sort_values('score',ascending=False,inplace=True)
df_second['score']=df_second['score']/10

c=0
for index,row in df_second.iterrows():
    if c==5:
        break
    if(row['title'] not in names):
        put_text(row['title'])
        put_text(row['score'])
        c+=1