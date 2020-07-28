class Family:  
    def __init__(self, name,age,sex,height): #creating a function
        self.name = name        #self is an instance of the class
        self.age = age
        self.sex = sex
        self.height = height

Asare = Family('Jida', 26, 'Female',"5'10 feet")
Bebli = Family('Carl', 24, 'Male', "6'0 feet")
print(Asare)
print(Bebli.__dict__)