arr = []

print("enter the length of the array: ")
n = int(input())

print("enter the values in the array : ")

for i in range(n):
    x = int(input())
    arr.append(x)
    
def selection_sort(arr,n):
    for i in range(n):
        Min=i
        for j in range(i+1,n):
            if arr[j]<arr[Min]:
                Min=j
        arr[i],arr[Min]=arr[Min],arr[i]
        print(arr)


selection_sort(arr,n)

