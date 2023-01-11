x= lambda a: a+10
print(x(10))


x= lambda a,b,c: a+b*c
print(x(1,5,67))


def func(x):
    return lambda a: a*x           #same function definition used for common to multiple function

mylamb= func(10)
mydumb= func(100)
print(mylamb(20))
print(mydumb(10))    
