import pandas as pand
import numpy as num_py

mark1=[22,330923,21,23,44]
mark2=[22,-13,4,-55,-332,12]

print(num_py.std(mark1),'mark 1 std')

print(num_py.std(mark2),'mark 2 std')


deviate={
    'Name':['jeya','baskaran','M'],
    'stdMarks1':[299,111,3333],
    'stdMarks2':[329,1123,345]
}

data_frame=pand.DataFrame(deviate)
print(data_frame,'Frame')
print(num_py.std(data_frame),'standard deivation for the data frame')