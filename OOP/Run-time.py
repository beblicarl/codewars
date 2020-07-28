class Family():
   def __init__(self,name,age,salary):  
       self.name = name
       self.age = age
       self.salary = salary
def earn(self):
        print('money')
 
class Son(Family):
 
   def earn(self):             #Run-time polymorphism
      print("no money")
 
class Daugther(Family):
 
   def earn(self):
       print("has money")

class Cousin(Family):
   pass
   
 
c = Son
c.earn(Family)
d = Daugther
d.earn(Family)
e = Cousin
print(e.earn(Family))
