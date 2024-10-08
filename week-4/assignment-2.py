"""
Create a Python program that multiplies the transpose of a given matrix by a scalar. The program should prompt the user to input the dimensions of the matrix, the elements of the matrix, and the scalar value. The program should then compute the transpose of the matrix, multiply it by the scalar, and print the resulting matrix.

Input:
The first input is an integer 𝑟 , the number of rows in the matrix.
The second input is an integer 𝑐 , the number of columns in the matrix.
The next 𝑟 lines each contain 𝑐 integers, representing the elements of the matrix.
The final input is an integer 𝑠, representing the scalar value.

Output Format:
The output consists of 𝑐 lines, each containing 𝑟 integers, representing the elements of the resulting matrix after multiplying the transpose of the original matrix by the scalar.

Example:

Input:

2
3
1 2 3
4 5 6
2

Output:
2 8
4 10
6 12
"""

r = int(input())
c = int(input())
m = []
for i in range(r):
  row = input().split(" ")
  for j in range(c):
    row[j] = int(row[j])
  m.append(row)
scalar = int(input())
# Matrix Transpose
tr = []
for i in range(c):
  row = []
  for j in range(r):
    row.append(scalar * m[j][i])
  tr.append(row)
#print(tr)
for i in range(c):
  for j in range(r):
    if (j == (r - 1)):
      print(tr[i][j])
    else:
      print(tr[i][j], end=" ")
