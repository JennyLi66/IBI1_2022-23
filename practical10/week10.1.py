Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def can_buy_house(value, salary):
...     affordability = salary*5
...     if value >= affordability:
...         return "Yes"
...     else:
...         return"No"
... 
...     
>>> print(can_buy_house(180000, 35000))
Yes
