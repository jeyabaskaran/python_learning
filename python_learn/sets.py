data={'data',2,'ddd','dummt'}
print(data)

dump=set(('daaa','daddh',23,2))
print(dump)


#access sets item

for x in data:
    print(x)

print('daaa' in dump)

#add items

data.add('new')
data.update(dump)

print(data)


#remove items in sets

data.remove('data') #if not exists in sets throw error
print(data)

#use discard instead of remove keyword
data.discard('ddkdndkd')
print(data)

dump2={'daa','new','financ',23,404,'daaa'}

set3=dump2.union(data)
print(set3,'final')

dump2.intersection_update(data)
dump2.symmetric_difference_update(data)
set4=dump2.symmetric_difference(data)
print(dump2,'set')
print(set4,'set4')