class Family(object):
    def __init__(self):   
        self.name = 1234
        self._age = 1234
        self.__sex = 1234
    
object1 = Family()
print(object1.name)
print(object1._age)
print(object1.__sex)