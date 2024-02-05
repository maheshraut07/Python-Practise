mahesh=[15,45,36,10,5]
print("list before sorting=",mahesh)
for i in range(0,len(mahesh)):
  
    for j in range(i+1,len(mahesh)):
        if(mahesh[i]>mahesh[j]):
           mahesh[i],mahesh[j]=mahesh[j],mahesh[i]
    i=i+1
           
print("list after sorting=",mahesh)
