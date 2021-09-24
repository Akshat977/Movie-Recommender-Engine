# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:17:41 2021

@author: aksha
"""

from pywebio.input import *
from pywebio.output import *
import numpy as np
import pandas as pd
put_text("SUGGESTING MOVIES WITH THE HIGHEST POPULARITY + RATING(WHICH HAS NOT YET BEEN WATCHED)")
data = input_group("Input Movies",[
  
  textarea('Text Area', rows=3, placeholder='Some text',name='name')
])

df_first=pd.read_csv('tmdb_5000_movies.csv')
df_second=pd.read_csv('movies.csv')
df_third=pd.read_csv('ratings.csv')

#naam=textarea('Text Area', rows=3, placeholder='Some text')
names=data['name'].split('\n')
df_first_cleaned=df_first[['id','popularity','vote_average','vote_count']]

R=df_first_cleaned['vote_average']
v=df_first_cleaned['vote_count']
C=df_first_cleaned['vote_average'].mean()
m=df_first_cleaned['vote_count'].quantile(0.70)
df_first_cleaned['W']=((R*v)+(C*m))/(v+m)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaled=scaler.fit_transform(df_first_cleaned[['popularity','W']])
df_first_scaled=pd.DataFrame(scaled)
df_first_scaled.columns=['popularity','W']

df_first_cleaned.drop(['popularity','W'],axis=1,inplace=True)
df_first_cleaned=pd.concat([df_first_cleaned,df_first_scaled],axis=1)

score=(df_first_cleaned['popularity']*0.5)+(df_first_cleaned['W']*0.5)
score=pd.DataFrame(score)
score.columns=['score']
df_first=pd.concat([df_first,score],axis=1)

df_first.sort_values('score',ascending=False,inplace=True)


c=0
for index,row in df_first.iterrows():
    if c==5:
        break
    if(row['title'] not in names):
        put_text(row['title'])
        c+=1 

