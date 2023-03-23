Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
cost=[1,8,15,7,5,14,43,40]
cost.sort()
print(cost)
[1, 5, 7, 8, 14, 15, 40, 43]
import numpy as np
import matplotlib.pyplot as plt
N = 8
cost = (1,8,15,7,5,14,43,40)
Olympics Game = (Los Angeles 1984,Seoul 1988,Barcelona 1992,Atlanta 1996,Sydney 2000,Athens 2003,Beijing 2008,London 2012)
SyntaxError: invalid syntax
>>> Olympics Games = (Los Angeles 1984,Seoul 1988,Barcelona 1992,Atlanta 1996,Sydney 2000,Athens 2003,Beijing 2008,London 2012)
SyntaxError: invalid syntax
>>> Olympics_Game = (Los Angeles 1984,Seoul 1988,Barcelona 1992,Atlanta 1996,Sydney 2000,Athens 2003,Beijing 2008,London 2012)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> ind = np.arange(N)
>>> width = 0.35
>>> pl = plt.bar(ind,cost,width)
>>> plt.ylable('cost')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    plt.ylable('cost')
AttributeError: module 'matplotlib.pyplot' has no attribute 'ylable'. Did you mean: 'table'?
>>> plt.title(Olympics Costs)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> plt.title('Olympics Costs')
Text(0.5, 1.0, 'Olympics Costs')
>>> plt.xticks(ind, ('1984,1988,1992,1996,2000,2003,2008,2012'))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    plt.xticks(ind, ('1984,1988,1992,1996,2000,2003,2008,2012'))
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/pyplot.py", line 1893, in xticks
    labels = ax.set_xticklabels(labels, minor=minor, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/axes/_base.py", line 74, in wrapper
    return get_method(self)(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/_api/deprecation.py", line 297, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/axis.py", line 1969, in set_ticklabels
    raise ValueError(
ValueError: The number of FixedLocator locations (8), usually from a call to set_ticks, does not match the number of labels (39).
>>> plt.show()
