#calling a class method from another class method

class ABC:
    def method1(self):
        print('this is method 1')
    def method2(self):
        print('this is method 2')
        self.method1()
s1=ABC()
s1.method2()
print('thank you')
