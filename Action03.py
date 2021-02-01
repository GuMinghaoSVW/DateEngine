# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:26:57 2021

@author: GuMinghao
"""

import pandas as pd

result= pd.read_csv('C:/Users/guminghao/Desktop/Python/car_complain.csv')


print(result)

result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result.columns)

problemdetail = result.columns[7:]
print(problemdetail)


df= result.groupby(['brand'])['id'].agg(['count'])
print(df)
print(df.sort_values('count',ascending=False))
# df2= result.groupby(['brand'])[problemdetail].agg(['count']) !!!!!!!!!!!!!!为啥不是count????????
# print(df2)
df2= result.groupby(['brand'])[problemdetail].agg(['sum'])
print(df2)
df2 = df.merge(df2, left_index=True, right_index=True, how='left')

# # 通过reset_index将DataFrameGroupBy => DataFrame
df2.reset_index(inplace=True)
print(df2)

df2= df2.sort_values('count', ascending=False)
print(df2)
print(df2.columns)

query = ('A13', 'sum')
print(df2.sort_values(query, ascending=False))
