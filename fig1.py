#coding=UTF-8
'''
处理用户行为数据，Residential-Profiles.csv

@author CCBurning
'''
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']

import matplotlib.ticker as mticker



df = pd.read_csv('Residential-Profiles-right.csv',header=1)
# print(df.dtypes)
df['Time'] = pd.to_datetime(df['Time'],format="%Y/%m/%d %H:%M")
df.set_index('Time',inplace=True)
# print(df.dtypes)


# print(df.head())


df['sum'] = df.sum(axis=1)
# print(df.dtypes)
print(df.head())


#时间轴直接为一年的每一个时刻
# fig,ax = plt.subplots()
# ax.plot(df.index,df['sum'])
# plt.show()


print(df.index[0])
a = df.index[0]
print(a.hour)
print(a.minute)
print(df.index[90])
a = df.index[90]
print(a.hour)
print(a.minute)

#建立横坐标一天时间的表格
seq = ['%02d:%02d' %(i,j) for i in range (0,24) for j in range(0,60,10)]
# print(seq)

df_day = pd.DataFrame(index=seq)
# print(df_day.info)
df_day['sum'] = 0.0
# print(df_day.dtypes)
# print("提取出来的列的信息")
# print(df.iloc[0:144,200])
for x in range(0,365):
    df_day['sum'] = df_day['sum'] + df.iloc[144*x:144*x+144,200].values

# print(df_day.head())

#时间轴直接为一天的每一个时刻
fig,ax = plt.subplots()
ax.plot(df_day.index,df_day['sum'])
plt.xticks(df_day.index,rotation=90)

for label in ax.xaxis.get_ticklabels()[::1]:
    label.set_visible(False)
for label in ax.xaxis.get_ticklabels()[::5]:
    label.set_visible(True)
plt.xlabel(U'时刻')
plt.ylabel(u'家庭负荷值（W）')
plt.title(u'某地区年度家庭负荷总量时刻分布')
# ax.tick_params(labeltop={'off','on','off','off','off'})

# ax.xaixs.setmajor_locater(df_day.index[0::2])
# ax.set_xticks([])
# ax.set_xlables([])
# plt.show()
print(df_day.index[0::2])

#分为四个季度四条曲线
df_day['1_sum'] = 0.0
for x in range(0,59):
    df_day['1_sum'] = df_day['1_sum'] + df.iloc[144*x:144*x+144,200].values
for x in range(334,365):
    df_day['1_sum'] = df_day['1_sum'] + df.iloc[144*x:144*x+144,200].values

df_day['2_sum'] = 0.0
for x in range(59,151):
    df_day['2_sum'] = df_day['2_sum'] + df.iloc[144*x:144*x+144,200].values

df_day['3_sum'] = 0.0
for x in range(151,243):
    df_day['3_sum'] = df_day['3_sum'] + df.iloc[144*x:144*x+144,200].values

df_day['4_sum'] = 0.0
for x in range(243,334):
    df_day['4_sum'] = df_day['4_sum'] + df.iloc[144*x:144*x+144,200].values


# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(df_day.index, df_day['1_sum'], 'k--', label='winter')
ax.plot(df_day.index, df_day['2_sum'], 'k:', label='spring')
ax.plot(df_day.index, df_day['3_sum'], 'k', label='summer')
ax.plot(df_day.index, df_day['4_sum'], 'r:', label='fall')

legend = ax.legend(loc='upper left', fontsize='x-large')
for label in ax.xaxis.get_ticklabels()[::1]:
    label.set_visible(False)
for label in ax.xaxis.get_ticklabels()[::5]:
    label.set_visible(True)
plt.xlabel(U'时刻')
plt.ylabel(u'家庭负荷值（W）')
plt.title(u'某地区年度家庭负荷总量时刻分布')
plt.xticks(rotation=90)
# plt.show()

#  #时间轴直接为一周的每一个时刻
df_copy = df
print(df_copy.index.dayofweek[:200])
df_copy.index = df_copy.index.dayofweek
#所有的周几聚合,一年功率的平均值
df_week = df_copy.groupby(df_copy.index).mean()
print(df_copy.groupby(df_copy.index).sum())

fig,ax = plt.subplots()
ax.plot(df_week.index,df_week['sum'])
plt.xticks([0,1,2,3,4,5,6], ['星期日','星期一','星期二','星期三','星期四','星期五','星期六'])
plt.xlabel(u'星期')
plt.ylabel(u'家庭负荷值（W）')
plt.title(u'某地区年度家庭负荷总量星期分布')
# plt.xticks(rotation=270)
plt.show()



