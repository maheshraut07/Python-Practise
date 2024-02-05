def insertion(arr,n):
    
    print (arr)
    for i in range (1,n):
        temp=arr[i]
        j=i-1
        while((j>=0) & (arr[j]>temp)):
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp
            print(arr)
    print(arr)
arr=[10,4,5,3,8]
n=len(arr)
insertion(arr,n)
