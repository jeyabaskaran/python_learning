#disctinories in python it's like an object(js)

disct={
    "key":1,
    "name":'pair',
    'subset':19,
    'dat':'2022/22/22'
}
print(disct['name'])

print(len(disct))

# use dict keyword to create dictionary

thisDisct=dict(name='fine',dump="dump",num=1)
print(thisDisct)


x=thisDisct.get('name')
print(x)

y=thisDisct.keys()
n=thisDisct.values()
print(y)
for z in y:
    print(z)

for w in n:
    print(w)


print(thisDisct.items())

for x,y in thisDisct.items():
    print(x,'',y)

for x in thisDisct.values():
    print(x)

for y in thisDisct.keys():
    print(y)

