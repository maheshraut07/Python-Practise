#object variable
#example 1
class student():
    serial_no=0                                   #class variable 
    def __init__(self,marks):                     #marks=object variable
        self.marks=marks                          #by init method
        student.serial_no=student.serial_no+1
        print(self.marks)
        print(student.serial_no)
s1=student(70)
s2=student(80)
object3=student(90)
print('==================================')


#example 2


class student():
    serial_no=0
    def display(self,marks):                        #by normal function method
        self.marks=marks
        student.serial_no=student.serial_no+1
        print(self.marks)
        print(student.serial_no)
s1=student()
s2=student()
s1.display(70)
s2.display(80)
print('=======================================')


