def Binesearch(arr,key):
    low=0
    high=len(arr)-1
    m=(low+high)//2
    if(key<arr[m]):
        high=m-1
            
    elif(key>arr[m]):
        low=m+1
        
    elif(key==arr[m]):
        print("element found")
    else:
        print("element not found")

    
        

print("\nHow many elements are there in array")
n=int(input())

array=[]
i=0
for i in range(n):
    print("\n enter the elements in the array")
    item=int(input())
    array.append(item)
    
print("resultant array is\n")
print(array)

print("\n enter the element which you want to search")
key=int(input())

Binesearch(array,key)
print("index is ",index(m))

