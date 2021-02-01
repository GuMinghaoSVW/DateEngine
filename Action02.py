# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:20:33 2021

@author: GuMinghao
"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame
data = {'Chinese': [66, 95, 93, 90,80], 'Math': [30, 98, 96, 77, 90], 'English': [65, 85, 92, 88, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
print(df1)
print(chr(9))
print(df2)
print(chr(9))
print(df2.describe())
# print(chr(9))
# print(df2.sum())
print(chr(9))

df2['Col_sum'] = df2.apply(lambda x: x.sum(), axis=1)

print(df2)
print(chr(9))

df4 = df2.sort_values('Col_sum', ascending=False)

print(df4)