class Grandmother(): #THis is the Superclass
    def __init__(self, name,age,sex,height): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

class Mother(Grandmother): #THis is the first generation child class
    def __init__(self, name,age,sex,height): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

class Daughter(Mother): #THis is the second generation child class
    def __init__(self, name,age,sex,height): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
Rose = Grandmother('Rose', 52, 'Female',"5'11 feet",)
Jida = Mother('Jida', 26, 'Female',"5'10 feet")

print(Rose.age)
print(Jida.height)
