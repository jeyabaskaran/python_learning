tup=('tup','data',1,2,4) #tuple creation
print(tup,'tup')
print(tup[1],'ind')

lis=tuple(('dkd','data',13,33)) #another way to create tuple
print(lis,'lis')

lett=('aaap',) #for single item must end with comma without comma it's just a string
print(len(tup))


if 'tup' in tup:
    print('yes')


#tuple is unchangeable if you need to add ,
#remove or update anything we need to convert tuple to list and change the items.
#we can add tuple with another tuple

tup2=('DA','DD')
tup+=tup2
print(tup)


#unpack tuple values

dump=('data','dummy','ddd',22,22)
(cos,*dumm)=dump
print(cos,'',dumm,'',dump)

print(dump.count(22),'count')

#loop

for x in dump:
    print(x)

for x in range(len(dump)):
    print(x)
    print(dump[x])