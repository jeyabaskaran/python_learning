import pandas as pand
import numpy as num_py


#sereies is the one dimensionaly array, it contains different types of data.
#we can convert list , tuple , and disctionary into series using series method.


#empty series

empty_series=pand.Series()
print(empty_series , 'empty series')


# we can create series using various inputs Dict, list, and scalar values
#before creating series we need to import numpy

arr_series=num_py.array(['p','a','n','d','a','s'])
print(pand.Series(arr_series),'arrary series')


# series with dict


dict_series={'x':'data','y':389,'z':'dummt'}     #for dict don't have indes so, it's take key as index
aff_series=pand.Series(dict_series) # x comes under 0 the position, same like another keys.
print(aff_series)
print(aff_series[0])



# series with scalar we can speicify our values to the index or we can sepecify the index name

scalar_series=pand.Series(4,index=[0,1,2,3,4]) #ex 1
print(scalar_series)

scalar_name=['dummy','data','for','loop','']
scalar_series2=pand.Series(scalar_name,['aa','bb','cc','dd','ddddd'])
print(scalar_series2) #ex2