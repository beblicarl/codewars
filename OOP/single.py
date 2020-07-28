class Mother:
    def __init__(self, name,age,sex,height): #This is the parent class
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

class Daughter(Mother): #THis is the child class
    def __init__(self, name,age,sex,height,status): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.status = status
Jida = Mother('Jida', 26, 'Female',"5'10 feet")
print(Jida.__dict__)

