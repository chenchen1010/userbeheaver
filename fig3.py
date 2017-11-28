#codeing=UTF-8

import pandas as pd
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']


df = pd.read_csv('PEV-Profiles-L2.csv',header=2)
# print(df.dtypes)
df['Time'] = pd.to_datetime(df['Time'],format="%Y/%m/%d %H:%M")
df.set_index('Time',inplace=True)
df_number = df.copy()
# print(df.dtypes)
# print(df.head())

# df_day = df
# print(str(df_day.index[36].hour)+':'+str(df_day.index[36].minute))
# df_day.set_index(df_day.index.hour,inplace=True)
# print("df_day.index的属性：")
# print(df_day.index)
# df_day = df_day.groupby(df_day.index).sum(axis=0)
# print(df_day.head(7))
# #聚合方法显示一周每个小时，集体不到分钟
# # df_day = df_day.groupby(df_day.index).sum()
# df_day['sum'] = df_day.sum(axis=1)
# fig,ax = plt.subplots()
# ax.plot(df_day.index,df_day['sum'])
# plt.xticks(rotation=90)
# plt.show()

#最终结果图
df['sum'] = df.sum(axis=1)


seq = ['%02d:%02d' %(i,j) for i in range (0,24) for j in range(0,60,10)]
df_day = pd.DataFrame(index=seq)
df_day['sum'] = 0.0
for x in range(0,365):
    df_day['sum'] = df_day['sum'] + df.iloc[144*x:144*x+144,348].values

#时间轴直接为一天的每一个时刻
fig,ax = plt.subplots()
ax.plot(df_day.index,df_day['sum'])
plt.xticks(df_day.index,rotation=90)

#分为四个季度四条曲线
df_day['1_sum'] = 0.0
for x in range(0,59):
    df_day['1_sum'] = df_day['1_sum'] + df.iloc[144*x:144*x+144,348].values
for x in range(334,365):
    df_day['1_sum'] = df_day['1_sum'] + df.iloc[144*x:144*x+144,348].values

df_day['2_sum'] = 0.0
for x in range(59,151):
    df_day['2_sum'] = df_day['2_sum'] + df.iloc[144*x:144*x+144,348].values

df_day['3_sum'] = 0.0
for x in range(151,243):
    df_day['3_sum'] = df_day['3_sum'] + df.iloc[144*x:144*x+144,348].values

df_day['4_sum'] = 0.0
for x in range(243,334):
    df_day['4_sum'] = df_day['4_sum'] + df.iloc[144*x:144*x+144,348].values

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(df_day.index, df_day['1_sum'], 'k--', label='winter')
ax.plot(df_day.index, df_day['2_sum'], 'k:', label='spring')
ax.plot(df_day.index, df_day['3_sum'], 'k', label='summer')
ax.plot(df_day.index, df_day['4_sum'], 'r:', label='fall')

legend = ax.legend(loc='upper left', fontsize='x-large')

plt.xticks(rotation=90)



#每天某一时刻充电汽车数量的直方图

# print(df_number.dtypes)
df_number = df_number/1920
# print(df_number.iloc[26])
# df_number.to_csv('df_number.csv',index=False)
# print(df_number.head(50))
df_number['sum'] = df_number.sum(axis=1)

df_number_day = pd.DataFrame(index=seq)
df_number_day['sum'] = 0
for x in range(0,365):
    df_number_day['sum'] = df_number_day['sum'] + df_number.iloc[144*x:144*x+144,348].values
# print(df_number.shape)
# print(df_number_day.shape)
# print(df_number_day.head(50))
#时间轴直接为一天的每一个时刻

# the histogram of the data
fig, ax = plt.subplots()
plt.bar(df_number_day.index, df_number_day['sum'])

plt.xlabel(U'时刻')
plt.ylabel(u'充电车数')
plt.title(u'某地区一年每天充电车数量')
plt.xticks(rotation=90)
plt.show()


