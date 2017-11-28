#字符串处理
s=[str(x) + ':' + str(y) for x in range(0, 24) for y in range(0, 60, 5)]
print(s)

s=pd.date_range('01:00:00', '02:00:00', freq= '5min')
print(s)

seq = ['%02d:%02d' %(i,j) for i in range (0,24) for j in range(0,60,10)]
print(seq)


#df按照index groupby聚合
df_copy.index = df_copy.index.dayofweek
#所有的周几聚合,一年功率的平均值
df_week = df_copy.groupby(df_copy.index).mean()

# Python基础-int和string互相转换

# int转成string，函数
int(string)
# string转成int，函数
str(number)

#matplotlib 中文乱码问题
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
import seaborn as sns
sns.set_style("darkgrid",{"font.sans-serif":['simhei', 'Arial']})
See more about seaborn.set or seaborn.set_style.

#将下周坐标标注和文本稀疏显示
for label in ax.xaxis.get_ticklabels()[::1]:
    label.set_visible(False)
for label in ax.xaxis.get_ticklabels()[::4]:
    label.set_visible(True)

#设定图标题x轴y轴坐标
plt.xlabel(U'时刻')
plt.ylabel(u'充电车数')
plt.title(u'某地区一年每天充电车数量')