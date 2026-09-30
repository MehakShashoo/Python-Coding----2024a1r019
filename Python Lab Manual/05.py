# Write a program to reverse every kth row in a matrix. 

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter row elements: ").split()))
    matrix.append(row)

k = int(input("Enter row you want to reverse: "))

for i in range(k - 1, rows, k):
    matrix[i].reverse()

print("Matrix after reversing every kth row:")

for row in matrix:
    print(row)