class a():                    #parent class
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
    
    def myPrint(self):
        print(self.name,self.age,self.graduationYear)


# x=a('name',34)
# x.myPrint()


class b(a):         #child class
    def __init__(self,name,age,year):
        self.name=name
        self.age=age
        self.graduationYear=year
        super().__init__()

    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of", self.graduationYear)

y=b('na,mmme','jeya',2019)
y.myPrint()
y.welcome()