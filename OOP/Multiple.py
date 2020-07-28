class Mother(): #this is a parent class
    def __init__(self, name,age,sex,height): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

class Father(): #This is also a parent class
    def __init__(self, name,age,sex,height,status):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.status = status

class Child(Mother,Father): #THis is the second generation child class
    def __init__(self, name,age,sex,height,status): 
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.status = status
Grace = Mother('Grace', 53, 'Female',"5'10 feet")
Harry = Father('Harry', 63, 'Female',"5'10 feet",'Married')

print(Grace.age)
print(Harry.status)