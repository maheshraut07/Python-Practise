#public and private methods(defines in the class)

class ABC:
    def __init__(self,value1,value2):
        self.var1=value1
        self.__var2=value2
    def update(self,value): #public method accesible from anywhere in the program
        self.var1=value
        self.__display()
    def __display(self):    #private method accessible from anywhere (double prefix underscore)
        print('var1=',self.var1)
        print('var2=',self.__var2)
s1=ABC(10,20)
s1.update(50)
