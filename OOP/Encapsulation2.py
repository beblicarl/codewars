class Family():
    def __init__(self):
        self.__maxearn = 1000000
    def earn(self):
        print("earning is:{}".format(self.__maxearn))
 
    def setmaxearn(self,earn):  #setter method used for accesing private class
        self.__maxearn = earn
 
son = Family()
son.earn()
 
son.__maxearn = 10000
son.earn()
 
son.setmaxearn(10000)
son.earn()