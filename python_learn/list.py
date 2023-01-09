


arr = ['1', '2', '3', '4', '5', 1]

arr.append('data') #append new list item
arr.insert(4,'dummy') # insert new item with sepecific index
print(arr,'append')

#arr.pop() # remove last item in list
arr.pop(1) # remove specific item in list
print(arr,'pop')

#del arr #remove entire list
#arr.clear() # clear list items only
#print(arr,'clear')


print(range(len(arr))) #find range with length

#for loop without index
for x in arr:
    print(x,'data')

# for loop with index
for x in range(len(arr)):
    print(arr[x], 'index', x)

#single line for loop syntax
    [print(arr[x], 'inded') for x in range(len(arr))]

#while loop

i=0
while(i<len(arr)):
    print(arr[i],'while')
    i=i+1
    