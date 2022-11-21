#creating matrice A
A_ROW = int(input("Enter the number of rows in matrice A: "))
A_COLUMN = int(input("Enter the number of columns in matrice A: "))
#initialize matrix
matrix_A = []
print("Input the entries rowwise: ")
#for user input
for i in range(A_ROW): #for loop for row entries
    a = []
    for j in range(A_COLUMN): #for loop for column entries
        a.append(int(input()))
    matrix_A.append(a)
    
#creating matrice B
 
B_ROW = int(input("Enter the number of rows in matrice B: "))
B_COLUMN = int(input("Enter the number of columns in matrice B: "))

matrix_B = []
print("Input the entries rowwise: ")
for i in range(B_ROW):
    b = []
    for j in range(B_COLUMN):
        b.append(int(input()))
    matrix_B.append(b)
    
#printing the matrix       
print("Matrix A:")
for i in range(A_ROW):
    for j in range(A_COLUMN):
        print(matrix_A[i][j], end= " ")
    print()
print("Matrix B:")
for i in range(B_ROW):
    for j in range(B_COLUMN):
        print(matrix_B[i][j], end= " ")
    print()


#creating matrixMul
def matrixMul(matrixA, matrixB):    
    global A_COLUMN, B_ROW
    #the number of columns in the first matrix must be equal to the number of rows in the second
    if (A_COLUMN != B_ROW):
        return "CANNOT MUTIPLY MATRIX A AND B. (the number of columns in the first matrix must be equal to the number of rows in the second)"
    else: 
        result = [[sum(a * b for a, b in zip(A_ROW, B_COL)) for B_COL in zip(*matrixB)] for A_ROW in matrixA]
        for r in result:
            print(r)

print("PRODUCT: ")
print(matrixMul(matrix_A, matrix_B))