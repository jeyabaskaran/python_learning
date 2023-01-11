try:
    print(101)
except NameError:
    print("no data found")
except:
    print("something went wrong")
else:
    print('hello')
finally:
    print('try is finished')

username=input('Enter userName:')
print(username,'username')

# x=1
# if x<0:
#     raise Exception("No values come under 0")

# if not type(x) is str:
#     raise TypeError('Erro should be found')