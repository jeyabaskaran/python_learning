#learn about basics in pandas



import pandas as pand

myDataSet={
    'Car':['Dummy','data','sofar',''],      #note the dictionary must contain the same count of values in eacy key
    'Price':[
        '1022','22324','239393','dddd'
    ]
}

print(pand.DataFrame(myDataSet))    
print(pand.__version__,'----version') #to find the version of pandas