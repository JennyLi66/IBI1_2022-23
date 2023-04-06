Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import pandas as os
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> os.chdir("/Users/jenny/IBI_2022-23
... /Users/jenny/IBI_2022-23
... 
SyntaxError: unterminated string literal (detected at line 1)
>>> os.chdir("/Users/jenny/IBI_2022-23/Practical7")
...          
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.chdir("/Users/jenny/IBI_2022-23/Practical7")
AttributeError: module 'pandas' has no attribute 'chdir'
>>> import pandas as pd
>>> import os
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> os.chdir
<built-in function chdir>
>>> os.chdir("/Users/jenny/IBI_2022-23/Practical7")
>>> os.getcwd("/Users/jenny/IBI_2022-23/Practical7")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    os.getcwd("/Users/jenny/IBI_2022-23/Practical7")
TypeError: posix.getcwd() takes no arguments (1 given)
>>> listdir("/Users/jenny/IBI_2022-23/Practical7")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    listdir("/Users/jenny/IBI_2022-23/Practical7")
NameError: name 'listdir' is not defined
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd("/Users/jenny/IBI_2022-23/Practical7")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    os.getcwd("/Users/jenny/IBI_2022-23/Practical7")
TypeError: posix.getcwd() takes no arguments (1 given)
os.getcwd("/Users/jenny/IBI_2022-23/Practical7")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    os.getcwd("/Users/jenny/IBI_2022-23/Practical7")
TypeError: posix.getcwd() takes no arguments (1 given)

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
describe()
         
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    describe()
NameError: name 'describe' is not defined
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
covid_data.iloc[0:1000:100,0:11]
         
           date     location  new_cases  new_deaths  total_cases  total_deaths
0    2019-12-31  Afghanistan          0           0            0             0
100  2020-03-27      Albania         28           1          174             6
200  2020-03-22      Andorra         13           0           88             0
300  2020-02-07      Armenia          0           0            0             0
400  2020-02-15    Australia          0           0           15             0
500  2020-02-23      Austria          0           0            0             0
600  2020-03-02   Azerbaijan          2           0            3             0
700  2020-03-04      Bahrain          2           0           49             0
800  2020-02-10      Belarus          0           0            0             0
900  2020-02-26      Belgium          0           0            1             0
covid_data.iloc[0:1000:2,0:11]
         
           date     location  new_cases  new_deaths  total_cases  total_deaths
0    2019-12-31  Afghanistan          0           0            0             0
2    2020-01-02  Afghanistan          0           0            0             0
4    2020-01-04  Afghanistan          0           0            0             0
6    2020-01-06  Afghanistan          0           0            0             0
8    2020-01-08  Afghanistan          0           0            0             0
..          ...          ...        ...         ...          ...           ...
990  2020-03-14      Bolivia          7           0           10             0
992  2020-03-17      Bolivia          1           0           11             0
994  2020-03-19      Bolivia          0           0           12             0
996  2020-03-21      Bolivia          4           0           19             0
998  2020-03-23      Bolivia          7           0           27             0

[500 rows x 6 columns]
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
my_columns= [Ture,True,False,True, False,False]
         
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    my_columns= [Ture,True,False,True, False,False]
NameError: name 'Ture' is not defined
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
covid_data.loc[every row where location is "Afghanistan","total_case"]
         
SyntaxError: invalid syntax. Perhaps you forgot a comma?
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
covid_data.loc[7996,"new_cases"]
         
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/range.py", line 345, in get_loc
    return self._range.index(new_key)
ValueError: 7996 is not in range

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    covid_data.loc[7996,"new_cases"]
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1096, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/frame.py", line 3886, in _get_value
    row = self.index.get_loc(index)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/range.py", line 347, in get_loc
    raise KeyError(key) from err
KeyError: 7996
covid_data.loc[345,"new_cases"]
2
covid_data.loc[7996,"new_cases"]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/range.py", line 345, in get_loc
    return self._range.index(new_key)
ValueError: 7996 is not in range

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    covid_data.loc[7996,"new_cases"]
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1096, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/frame.py", line 3886, in _get_value
    row = self.index.get_loc(index)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/range.py", line 347, in get_loc
    raise KeyError(key) from err
KeyError: 7996
covid_data.iloc[7996,2]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    covid_data.iloc[7996,2]
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1096, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/frame.py", line 3877, in _get_value
    return series._values[index]
IndexError: index 7996 is out of bounds for axis 0 with size 7996
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
bool("Afghanistan")
True
Afghanistan=True
if not Afghanistan=False
SyntaxError: invalid syntax
not Afghanistan
False
covid_data.loc[True,:]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    covid_data.loc[True,:]
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1097, in __getitem__
    return self._getitem_tuple(key)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1280, in _getitem_tuple
    return self._getitem_lowerdim(tup)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1000, in _getitem_lowerdim
    section = self._getitem_axis(key, axis=i)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1342, in _getitem_axis
    self._validate_key(key, axis)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1151, in _validate_key
    raise KeyError(
KeyError: 'True: boolean label can not be used without a boolean index'
0:81=True
SyntaxError: illegal target for annotation
Afghanistan=True
covid_data.loc["Afghanistan",:]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    covid_data.loc["Afghanistan",:]
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1097, in __getitem__
    return self._getitem_tuple(key)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1280, in _getitem_tuple
    return self._getitem_lowerdim(tup)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1000, in _getitem_lowerdim
    section = self._getitem_axis(key, axis=i)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1343, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexing.py", line 1293, in _get_label
    return self.obj.xs(label, axis=axis)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/generic.py", line 4095, in xs
    loc = index.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/range.py", line 349, in get_loc
    raise KeyError(key)
KeyError: 'Afghanistan'
plt.plot(world_dates,world_new_cases,'b+')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    plt.plot(world_dates,world_new_cases,'b+')
NameError: name 'world_dates' is not defined
import numpy as np
import matplotlib.pyplot as plt

