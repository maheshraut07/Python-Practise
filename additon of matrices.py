m=int(input("enter row"))
n=int(input("enter col"))
a=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(int(input("entr elem.")))
    a.append(l)
print(a)
b=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(int(input("entr elem.")))
    b.append(l)
print(b)

res=[]
print("\nmatrices addition is ")
for i in range(m):
    l=[]
    for j in range(n):
        l.append(a[i][j]+b[i][j])
    res.append(l)
print(res)
