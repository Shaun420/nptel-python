"""
Create a Python program that checks whether a given square matrix is skew-symmetric. A matrix is skew-symmetric if its transpose is equal to the negative of the matrix itself, i.e AT=−A  .The program should prompt the user to input the dimensions of the matrix and then input the matrix elements. The program should then determine whether the matrix is skew-symmetric and print 1 if it is, otherwise print 0.

Input Format:
The first input is an integer r , the number of rows and columns in the matrix.
The next r lines each contain r integers, representing the elements of each row of the matrix.

Output Format:
The output is 1 if a matrix is skew-symmetric, otherwise 0.

Example:

Input:

3
0 2 -1
-2 0 -4
1 4 0

Output:
1
"""

n = int(input())
m = []
for i in range(n):
  row = list(map(int, input().split(" ")))
  m.append(row)
tr = []
for i in range(n):
  row = []
  for j in range(n):
    row.append(m[j][i])
  tr.append(row)
for i in range(n):
  for j in range(n):
    m[i][j] = -m[i][j]
if (m == tr):
  print(1, end="")
else:
  print(0, end="")
