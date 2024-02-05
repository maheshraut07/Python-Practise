x = int(input('Enter first number='))
y = int(input('enter second number='))
z = int(input('enter third number='))
def func(a,b,c):

    '''program for finding greatest among three numbers'''
    
    if (a==b==c):
        print('all three numbers are equal')

    elif (a==b) :
        print('a and b are equal')
    
    elif (b==c) :
        print('b and c are equal')
    
    elif (a==c):
        print('a and c are equal')

    elif(a>b & a>c):
        print('a is greatest number')
      
    elif(b>a & b>c):
        print('b is greatest number')

    else:
        print('c is greatest number')

func(x,y,z)
print(func.__doc__)
        
    
