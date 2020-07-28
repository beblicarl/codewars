class Son():
    def name(self):
        print("I go by the name Carl")  

    def age(self):
        print("I'm 26 years old")
 
    def car(self):
        print("and I own a black Elantra")
 
class Daughter():
    def name(self):
        print("Rose is her name")
 
    def age(self):
        print("She is 17 years old")
 
    def car(self):
        print("and she owns a red Toyota")


 
def func(obj):  #Method Overloading
    obj.name()
    obj.age()
    obj.car()
 
Carl = Son()
Rose = Daughter()
 
func(Carl)
func(Rose)