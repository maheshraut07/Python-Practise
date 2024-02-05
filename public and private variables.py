#public and private variable

class ABC:
    def __init__(self,marks1,marks2): #when object created __init__ method invoked
        self.var1=marks1             #public variable(defined in the class can be accessed from anywhere)
        self.__var2=marks2       #private variable(double underscore prefix, accesible only in the class)
    def display(self):
        print('var1=',self.var1)
        print('var2=',self.__var2)
s1=ABC(10,20)
s1.display()
print('var1=',s1.var1)
print('var2=',s1._ABC__var2) #error will be produced because of __var2 is private variable and can be only
                           #be accesible in the class to access private variable in the class
                           #we can use syntax as (object._classname__private variable)

                                    
