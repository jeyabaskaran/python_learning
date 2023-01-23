import pandas as pand
import numpy as num_py

a=pand.Series(['java','c','c++',num_py.nan])
a.map({'java':'Core','c':'Dummy'})
print(a.map({'java':'Core','c':'Dummy'}))
print(a.map('I like {}'.format))
print(a.map('I like {}'.format,na_action='ignore'),'na_action=ignore')