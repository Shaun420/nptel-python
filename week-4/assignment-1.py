"""
Create a Python program that identifies the presence of a "saddle point" in a given matrix. A saddle point is defined as an element in the matrix that is the smallest in its row and the largest in its column. The matrix is represented as a nested list, where each nested list corresponds to a row of the matrix. The program should determine if at least one saddle point exists in the matrix. If a saddle point is found, the program/function should print 1; otherwise, it should print 0.

Input Format:
The first input is an integer r , the number of rows in the matrix.
The second input is an integer c, the number of columns in the matrix.
The next r lines each contain c integers, representing the elements of each row of the matrix.

Output Format:
The output is 1 if a saddle point exists, otherwise 0.

Example:

Input:

3
3
2 0 3
2 1 4
4 2 6

Output:
1
"""

r = int(input())
c = int(input())
m = []
for i in range(r):
  row = input().split(" ")
  for j in range(len(row)):
    x = int(row[j])
    row[j] = x
  m.append(row)

found = False
for i in range(r):
  min = 1000
  count = 0
  col = -1
  for j in range(c):
    if (m[i][j] < min):
      count = 1
      min = m[i][j]
      col = j
    elif (m[i][j] == min):
      count += 1
  if count > 1:
    continue
  max = 0
  count = 0
  row = -1
  for j in range(r):
    if (m[j][col] > max):
      count = 1
      max = m[j][col]
      row = j
    elif (m[j][col] == max):
      count += 1
  if count > 1:
    continue
  if (row == i):
    found = True

if (found == True):
  print("1", end="")
else:
  print("0", end="")
