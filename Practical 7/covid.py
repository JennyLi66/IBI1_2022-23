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
