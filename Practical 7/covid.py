Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import os
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> os.chdir
<built-in function chdir>
>>> os.chdir("/Users/jenny/IBI_2022-23/Practical7")
os.getcwd()
'/Users/jenny/IBI_2022-23/Practical7'

os.listdir()
['full_data.csv']
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
         date     location  new_cases  new_deaths  total_cases  total_deaths
0  2019-12-31  Afghanistan          0           0            0             0
1  2020-01-01  Afghanistan          0           0            0             0
2  2020-01-02  Afghanistan          0           0            0             0
3  2020-01-03  Afghanistan          0           0            0             0
4  2020-01-04  Afghanistan          0           0            0             0
covid_data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7996 entries, 0 to 7995
Data columns (total 6 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   date          7996 non-null   object
 1   location      7996 non-null   object
 2   new_cases     7996 non-null   int64 
 3   new_deaths    7996 non-null   int64 
 4   total_cases   7996 non-null   int64 
 5   total_deaths  7996 non-null   int64 
dtypes: int64(4), object(2)
memory usage: 374.9+ KB
  
covid_data.describe()
         
          new_cases   new_deaths    total_cases  total_deaths
count   7996.000000  7996.000000    7996.000000   7996.000000
mean     194.546773     9.322661    2441.369060     97.977239
std     2083.395028   108.183439   22375.617031   1023.038977
min       -9.000000     0.000000       0.000000      0.000000
25%        0.000000     0.000000       0.000000      0.000000
50%        0.000000     0.000000       3.000000      0.000000
75%        8.000000     0.000000      60.000000      0.000000
max    65162.000000  3698.000000  777798.000000  37272.000000
covid_data.iloc[0,1]
         
'Afghanistan'
covid_data.iloc[2,0:5]
         
date            2020-01-02
location       Afghanistan
new_cases                0
new_deaths               0
total_cases              0
Name: 2, dtype: object
covid_data.iloc[0:2,:]
         
         date     location  new_cases  new_deaths  total_cases  total_deaths
0  2019-12-31  Afghanistan          0           0            0             0
1  2020-01-01  Afghanistan          0           0            0             0
covid_data.iloc[0:10:2,0:5]
         
         date     location  new_cases  new_deaths  total_cases
0  2019-12-31  Afghanistan          0           0            0
2  2020-01-02  Afghanistan          0           0            0
4  2020-01-04  Afghanistan          0           0            0
6  2020-01-06  Afghanistan          0           0            0
8  2020-01-08  Afghanistan          0           0            0


covid_data.iloc[0:1000:100,0:2]
         
           date     location
0    2019-12-31  Afghanistan
100  2020-03-27      Albania
200  2020-03-22      Andorra
300  2020-02-07      Armenia
400  2020-02-15    Australia
500  2020-02-23      Austria
600  2020-03-02   Azerbaijan
700  2020-03-04      Bahrain
800  2020-02-10      Belarus
900  2020-02-26      Belgium
covid_data.iloc[0:1000:100,0:1]
         
           date
0    2019-12-31
100  2020-03-27
200  2020-03-22
300  2020-02-07
400  2020-02-15
500  2020-02-23
600  2020-03-02
700  2020-03-04
800  2020-02-10
900  2020-02-26
covid_data.iloc[0:1000:100,0:0]
         
Empty DataFrame
Columns: []
Index: [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
covid_data.iloc[0:3,[0,1,3]]
         
         date     location  new_deaths
0  2019-12-31  Afghanistan           0
1  2020-01-01  Afghanistan           0
2  2020-01-02  Afghanistan           0

my_columns=[True,True,False,True,False,False]
         
covid_data.iloc[0:3,my_columns]
         
         date     location  new_deaths
0  2019-12-31  Afghanistan           0
1  2020-01-01  Afghanistan           0
2  2020-01-02  Afghanistan           0
covid_data.loc[2:4,"date"]
         
2    2020-01-02
3    2020-01-03
4    2020-01-04
Name: date, dtype: object
covid_data.loc[0:81,"total_cases"]
         
0       0
1       0
2       0
3       0
4       0
     ... 
77     75
78     91
79    106
80    114
81    141
Name: total_cases, Length: 82, dtype: int64

covid_data.iloc[0:1000:100,1]
         
0      Afghanistan
100        Albania
200        Andorra
300        Armenia
400      Australia
500        Austria
600     Azerbaijan
700        Bahrain
800        Belarus
900        Belgium
Name: location, dtype: object

covid_data.iloc[-1,2]
0
covid_data.loc[-1,"new_cases"]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/range.py", line 345, in get_loc
    return self._range.index(new_key)
ValueError: -1 is not in range

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    covid_data.loc[-1,"new_cases"]
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1096, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/frame.py", line 3886, in _get_value
    row = self.index.get_loc(index)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/range.py", line 347, in get_loc
    raise KeyError(key) from err
KeyError: -1
covid_data.loc[7995,"new_cases"]
0
covid_data.iloc[7995,2]
0
covid_data.loc[7995,"location"]
'Zimbabwe'
covid_data.loc[7995,"new_deaths"]
0
covid_data.loc[:,"location"]
0       Afghanistan
1       Afghanistan
2       Afghanistan
3       Afghanistan
4       Afghanistan
           ...     
7991       Zimbabwe
7992       Zimbabwe
7993       Zimbabwe
7994       Zimbabwe
7995       Zimbabwe
Name: location, Length: 7996, dtype: object

row = covid_data.loc[covid_data['location']=='Afghanistan']
                
print(row)
                
          date     location  new_cases  new_deaths  total_cases  total_deaths
0   2019-12-31  Afghanistan          0           0            0             0
1   2020-01-01  Afghanistan          0           0            0             0
2   2020-01-02  Afghanistan          0           0            0             0
3   2020-01-03  Afghanistan          0           0            0             0
4   2020-01-04  Afghanistan          0           0            0             0
..         ...          ...        ...         ...          ...           ...
77  2020-03-27  Afghanistan          0           0           75             1
78  2020-03-28  Afghanistan         16           1           91             2
79  2020-03-29  Afghanistan         15           1          106             3
80  2020-03-30  Afghanistan          8           1          114             4
81  2020-03-31  Afghanistan         27           0          141             4

[82 rows x 6 columns]

covid_data[covid_data['location']=='Afghanistan']
                
          date     location  new_cases  new_deaths  total_cases  total_deaths
0   2019-12-31  Afghanistan          0           0            0             0
1   2020-01-01  Afghanistan          0           0            0             0
2   2020-01-02  Afghanistan          0           0            0             0
3   2020-01-03  Afghanistan          0           0            0             0
4   2020-01-04  Afghanistan          0           0            0             0
..         ...          ...        ...         ...          ...           ...
77  2020-03-27  Afghanistan          0           0           75             1
78  2020-03-28  Afghanistan         16           1           91             2
79  2020-03-29  Afghanistan         15           1          106             3
80  2020-03-30  Afghanistan          8           1          114             4
81  2020-03-31  Afghanistan         27           0          141             4

[82 rows x 6 columns]
covid_data['location']=='Afghanistan'
                
0        True
1        True
2        True
3        True
4        True
        ...  
7991    False
7992    False
7993    False
7994    False
7995    False
Name: location, Length: 7996, dtype: bool

import numpy as np
new_cases_mean=np.mean(new_data[new_data['date']=='2020-03-31']['new_cases'])
new_deaths_mean=np.mean(new_data[new_data['date']=='2020-03-31']['new_deaths'])
print(new_cases_mean)
640.4615384615385
print(new_deaths_mean)
37.92820512820513
print(new_data)
            date  new_cases  new_deaths
81    2020-03-31         27           0
104   2020-03-31         11           2
191   2020-03-31         57           2
209   2020-03-31         36           2
219   2020-03-31          0           0
...          ...        ...         ...
7791  2020-03-31         16           2
7879  2020-03-31          1           0
7971  2020-03-31      62445        3698
7984  2020-03-31          6           0
7995  2020-03-31          0           0

[195 rows x 3 columns]
mean_values=np.mean(new_data[new_data['date']=='2020-03-31'][['new_cases','new_deaths']],axis=0)
print(mean_values)
new_cases     640.461538
new_deaths     37.928205
dtype: float64

import matplotlib.pyplot as plt
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
ax1.boxplot(data_31_Mar['new_cases'])
{'whiskers': [<matplotlib.lines.Line2D object at 0x13d02fe50>, <matplotlib.lines.Line2D object at 0x13d03d050>], 'caps': [<matplotlib.lines.Line2D object at 0x138b2df50>, <matplotlib.lines.Line2D object at 0x13cfff9d0>], 'boxes': [<matplotlib.lines.Line2D object at 0x138aaddd0>], 'medians': [<matplotlib.lines.Line2D object at 0x13d038ad0>], 'fliers': [<matplotlib.lines.Line2D object at 0x13d01aa90>], 'means': []}
ax2.boxplot(data_31_Mar['new_deaths'])
{'whiskers': [<matplotlib.lines.Line2D object at 0x11d552550>, <matplotlib.lines.Line2D object at 0x13d03ddd0>], 'caps': [<matplotlib.lines.Line2D object at 0x13d03e2d0>, <matplotlib.lines.Line2D object at 0x13d03f6d0>], 'boxes': [<matplotlib.lines.Line2D object at 0x13d02c910>], 'medians': [<matplotlib.lines.Line2D object at 0x13d054390>], 'fliers': [<matplotlib.lines.Line2D object at 0x13d054e90>], 'means': []}
# 设置箱型图标题和x轴标签
ax1.set_title('New Cases on 31 Mar')
Text(0.5, 1.0, 'New Cases on 31 Mar')
ax1.set_xlabel('Cases')
Text(0.5, 51.44444444444443, 'Cases')
ax2.set_title('New Deaths on 31 Mar')
Text(0.5, 1.0, 'New Deaths on 31 Mar')
ax2.set_xlabel('Deaths')
Text(0.5, 51.44444444444443, 'Deaths')
plt.show()
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/jenny/IBI_2022-23/Practical7")
covid_data=pd.read_csv('full_data.csv')
new_cases=covid_data.groupby(['date']).sum()['new_cases']
new_deaths=covid_data.groupby(['date']).sum()['new_deaths']
new_cases= new_cases.sort_index()
new_deaths=new_deaths.sort_index()
#绘制新病例时间图
plt.plot(new_cases.index, new_cases.values, label='new_cases')
[<matplotlib.lines.Line2D object at 0x11c1f5350>]
#绘制新死亡病例时间图
plt.plot(new_deaths.index, new_deaths.values, label='new_cases')
[<matplotlib.lines.Line2D object at 0x11e471d90>]
#添加图表标题，x轴和y轴标签等
plt.title('Global New Cases and Deaths Over Time')
Text(0.5, 1.0, 'Global New Cases and Deaths Over Time')
plt.xlabel('Date')
Text(0.5, 47.04444444444444, 'Date')
plt.ylabel('Number of Cases')
Text(23.069444444444432, 0.5, 'Number of Cases')
plt.xticks(rotation=45)
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [Text(0, 0, '2019-12-31'), Text(1, 0, '2020-01-01'), Text(2, 0, '2020-01-02'), Text(3, 0, '2020-01-03'), Text(4, 0, '2020-01-04'), Text(5, 0, '2020-01-05'), Text(6, 0, '2020-01-06'), Text(7, 0, '2020-01-07'), Text(8, 0, '2020-01-08'), Text(9, 0, '2020-01-09'), Text(10, 0, '2020-01-10'), Text(11, 0, '2020-01-11'), Text(12, 0, '2020-01-12'), Text(13, 0, '2020-01-13'), Text(14, 0, '2020-01-14'), Text(15, 0, '2020-01-15'), Text(16, 0, '2020-01-16'), Text(17, 0, '2020-01-17'), Text(18, 0, '2020-01-18'), Text(19, 0, '2020-01-19'), Text(20, 0, '2020-01-20'), Text(21, 0, '2020-01-21'), Text(22, 0, '2020-01-22'), Text(23, 0, '2020-01-23'), Text(24, 0, '2020-01-24'), Text(25, 0, '2020-01-25'), Text(26, 0, '2020-01-26'), Text(27, 0, '2020-01-27'), Text(28, 0, '2020-01-28'), Text(29, 0, '2020-01-29'), Text(30, 0, '2020-01-30'), Text(31, 0, '2020-01-31'), Text(32, 0, '2020-02-01'), Text(33, 0, '2020-02-02'), Text(34, 0, '2020-02-03'), Text(35, 0, '2020-02-04'), Text(36, 0, '2020-02-05'), Text(37, 0, '2020-02-06'), Text(38, 0, '2020-02-07'), Text(39, 0, '2020-02-08'), Text(40, 0, '2020-02-09'), Text(41, 0, '2020-02-10'), Text(42, 0, '2020-02-11'), Text(43, 0, '2020-02-12'), Text(44, 0, '2020-02-13'), Text(45, 0, '2020-02-14'), Text(46, 0, '2020-02-15'), Text(47, 0, '2020-02-16'), Text(48, 0, '2020-02-17'), Text(49, 0, '2020-02-18'), Text(50, 0, '2020-02-19'), Text(51, 0, '2020-02-20'), Text(52, 0, '2020-02-21'), Text(53, 0, '2020-02-22'), Text(54, 0, '2020-02-23'), Text(55, 0, '2020-02-24'), Text(56, 0, '2020-02-25'), Text(57, 0, '2020-02-26'), Text(58, 0, '2020-02-27'), Text(59, 0, '2020-02-28'), Text(60, 0, '2020-02-29'), Text(61, 0, '2020-03-01'), Text(62, 0, '2020-03-02'), Text(63, 0, '2020-03-03'), Text(64, 0, '2020-03-04'), Text(65, 0, '2020-03-05'), Text(66, 0, '2020-03-06'), Text(67, 0, '2020-03-07'), Text(68, 0, '2020-03-08'), Text(69, 0, '2020-03-09'), Text(70, 0, '2020-03-10'), Text(71, 0, '2020-03-11'), Text(72, 0, '2020-03-12'), Text(73, 0, '2020-03-13'), Text(74, 0, '2020-03-14'), Text(75, 0, '2020-03-15'), Text(76, 0, '2020-03-16'), Text(77, 0, '2020-03-17'), Text(78, 0, '2020-03-18'), Text(79, 0, '2020-03-19'), Text(80, 0, '2020-03-20'), Text(81, 0, '2020-03-21'), Text(82, 0, '2020-03-22'), Text(83, 0, '2020-03-23'), Text(84, 0, '2020-03-24'), Text(85, 0, '2020-03-25'), Text(86, 0, '2020-03-26'), Text(87, 0, '2020-03-27'), Text(88, 0, '2020-03-28'), Text(89, 0, '2020-03-29'), Text(90, 0, '2020-03-30'), Text(91, 0, '2020-03-31')])
plt.legend()
<matplotlib.legend.Legend object at 0x11e4cf490>
plt.show()

