def add_matrix(arr1,arr2):
    result = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    print("The Addition of Two Matrices...")
    print(result)
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
arr1 = []
for row in range(row_num):
    for col in range(col_num):
        item = int(input("Enter the elements in first matrix: "))
        arr1[row][col]= item
    
print("The first matrix is...")
print(arr1)
arr2 = []
for row in range(row_num):
    for col in range(col_num):
        item = int(input("Enter the elements in second matrix: "))
        arr2[row][col]= item
        
print("The second matrix is...")
print(arr2)
#Driver Code
add_matrix(arr1,arr2,)
