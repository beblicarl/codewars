from abc import ABC,abstractmethod
class Family(ABC):
    @abstractmethod
    def Son(self,name,age,salary):    #Abstraction
        pass
 
class Daughter(Family):
    def Son(self,age):
        print("Son is Carl")
 
Deborah = Daughter()
Deborah.Son(age)