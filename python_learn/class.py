class myclass():  # class creation
    x = 5


p1 = myclass()  # object creation
print(p1.x)


class samp():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = samp('jb', 'sa')
print(p1, 'without _str_function')  # without string representation
print(p1.name, p1.age)


class test():                       
    def __init__(data, name, age): #keyword self is the default one, we can whatever name we want, but that represent in first params
        data.name = name
        data.age = age

    def __str__(data):
        return f"{data.name} {data.age}"  # with str representation


p2 = test('jeya', '36')
print(p2, 'with _str_ function ')
