# function display a matrix
def display(matrix):
    for row in matrix:
        for element in row:
            print(element, end =" ")
            print()
# function to convert the matrix
# into a sparse matrix
def convert(matrix):
    SP =[]
# searching values greater
# than zero
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0 :
# creating a temporary sublist
                temp = []
# appending row value, column
# value and element into the

# sublist
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
# appending the sublist into
# the sparse matrix list
                SP.append(temp)
# displaying the sparse matrix
print("\nSparse Matrix: ")
print("Row Col Non_Zero_Value")
display(SP)
# Driver code
#Original Matrix
A =[ [10, 0, 0, 0],
    [0, 20, 0, 0],
    [0, 0, 30, 0],
    [0, 0, 0, 40],
    [0, 50, 0, 0]]
# displaying the matrix
display(A)
# converting the matrix to sparse
convert(A)
O
