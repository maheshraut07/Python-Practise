#calculator
print('calculator')
print('select operations')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.num1 to the power num2')
print('6.factorial of a number (num1!)')
choice=input('Enter choice(1/2/3/4/5/6)=')
if choice==('1'or'2'or'3'or'4'or'5'):
    num1=float(input('enter first number='))
    num2=float(input('enter second number='))
else:
    num=int(input('enter number='))
if choice=='1':
    print('Addition=',num1+num2)
elif choice=='2':
    print('Subtraction=',num1-num2)
elif choice=='3':
    print('multiplication=',num1*num2)
elif choice=='4':
    print('division=',num1/num2)
elif choice=='5':
    print('num1 to the power num2=',num1**num2)
elif choice=='6':
    fac=1
    i=1
    while i<=num:
        fac=fac*i
        i=i+1
        print('factorial of',num,'is=',fac)
    
