#program to find a fibonacci seqence of a number
n_terms = int(input('how many terms do you want='))
n1=0
n2=1
count=0
if (n_terms <=0):
    print('please enter the value')
elif(n_terms==1):
    print(n1)
else:
    while count<n_terms:
        print('n')
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
