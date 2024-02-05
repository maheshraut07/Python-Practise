row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
dim_num = int(input("Input number of dimensions: "))
arr1 =[]#creating an empty list
for dim in range(dim_num):
    arr1.append([])
    for row in range(row_num):
        arr1[dim].append([])
        for col in range(col_num):
            item = int(input("Enter Element: "))
            arr1[dim][row].append(item)
print("\n Elements in 3D Array are...")
for dim in range(dim_num):
    for row in range(row_num):
        for col in range(col_num):
            print(arr1[dim][row][col])
print()
print("——————-")
