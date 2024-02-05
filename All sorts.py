
def bubble_sort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)  

def selection_sort(arr,n):
    for i in range(n):
        Min=i
        for j in range(i+1,n):
            if arr[j]<arr[Min]:
                Min=j
            arr[i],arr[Min]=arr[Min],arr[i]
        print(arr)

def Insertion_sort(arr,n):
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    print (arr)


    
                
            
arr = []

print("enter the length of the array: ")
n = int(input())

print("enter the values in the array : ")

for i in range(n):
    x = int(input())
    arr.append(x)

#bubble_sort(arr,n)
selection_sort(arr,n)
#Insertion_sort(arr,n)