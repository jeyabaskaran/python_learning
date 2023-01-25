import pandas as pand

#empty data frame

info=pand.DataFrame()
print(info)

#dataFrame with list

info=pand.DataFrame(['data','margin','listData'])
print(info)

#dataFrame from dict with ndarray/lists

dic_t={'id':[1,2,3,4,5],'name':['jb','sudhan','sam','hari','sat'],'mark':[122,4222,4454,555,3332]}
info=pand.DataFrame(dic_t)
info['result']=['pass','fail','pass','pass','fail']  # able to add new column 
print(info)


#data frame from dict of series 

ser={'one':pand.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
'two':pand.Series([1,2,3,4,5,6,7],index=['a','b','c','d','e','f','g'])}

info=pand.DataFrame(ser)
print(info)
print(info['one']) # we can get the particulary column data with dataFrame

info['three']=pand.Series([1,2,3,4],index=['a','b','c','d']) # adding new column with series

info['four']=info['three']+info['one']  # able to merge the two columns into new column

print(info)

del info['one'] # delete the one particular column

info.pop('two') # we can delete columns with even del or pop() keyword, 
                #if all columns are deleted, it's like a empty data frame
print(info)


print(info.loc['a'])  # we can fetch the particular row data with passing row lable
print(info.iloc[5])   # or we can fetch the row with the passing index to the iloc method


print(info[2:5])  # we can splice the row and columns with ':' operator
print(info)
info2=pand.DataFrame([[1,2],[2,3]],columns=['three','four']) 


info=info.append(info2)  #add new row to the existing data frame

info=info.drop('a') # delete a particular row with drop()

print(info)



