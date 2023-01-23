import pandas as pand
import numpy as num_py

ind=pand.Index([1,3,3,1,1,4,5,num_py.nan]) 
print(ind.value_counts(dropna=False))  #its return the exact count of the gitven data


ine=pand.Series(['a','a','a',1,2,3,4,4,4,4])
print(ine.value_counts(normalize=True))       #it's return like how many frequencies of the data 


