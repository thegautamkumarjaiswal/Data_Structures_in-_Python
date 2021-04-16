# Read a 2d array from user. #
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the numbers of columns: "))

matrix = []
print("Enter the entries row_wise: ")

for i in range(rows):
    n = []
    for j in range(columns):
        n.append(int(input()))
    matrix.append(n)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()

# store in sparse matrix. #
size = 0

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] != 0:
            size +=1

rows, columns = (3, size)
compact_matrix = [[0 for i in range(columns)] for j in range(rows)]

k = 0
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] != 0:
            compact_matrix[0][k] = i
            compact_matrix[1][k] = j
            compact_matrix[2][k] = matrix[i][j]
            k += 1

# print final array. #
for i in compact_matrix:
    print(i)

