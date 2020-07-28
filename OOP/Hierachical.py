class Mother(): #This is the parent class
    def __init__(self, name,age,sex,height): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

class Daughter(Mother): #This is a child class
    def __init__(self, name,age,sex,height): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

class Son(Mother): #This is also a child class
    def __init__(self, name,age,sex,height): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
Deborah = Mother('Deborah', 26, 'Female',"5'10 feet")
Carl = Mother('Carl', 26, 'male',"6'0 feet")

print(Deborah.height)
print(Carl.age)