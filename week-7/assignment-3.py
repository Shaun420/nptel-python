"""
Question

Write a Python program that takes a matrix of size r x c as input, where r is the number of rows and c is the number of columns. The program should check if the matrix is binary (i.e., all elements are either 0 or 1) and if it is symmetric (i.e., the matrix is equal to its transpose).

The program should output:

    11 if the matrix is both binary and symmetric,
    10 if the matrix is binary but not symmetric,
    01 if the matrix is not binary but symmetric,
    00 if the matrix is neither binary nor symmetric.

Input Format:

    The first line contains an integer r representing the number of rows.
    The second line contains an integer c representing the number of columns.
    The next r lines each contain c space-separated integers representing the elements of the matrix.

Output Format:

    The output consists of a single string (either 11, 10, 01, or 00) as per the conditions mentioned above.

Example:

Input:
3
3
1 0 1
0 1 0
1 0 1

Output:
11
"""

r = int(input())
c = int(input())
m = []

for i in range(r):
  row = input().split(" ")
  row = list(map(int, row))
  m.append(row)

sym = "1"
binary = "1"
for i in range(r):
  for j in range(c):
    if (m[i][j] != m[j][i]):
      sym = "0"
    if (m[i][j] != 0 and m[i][j] != 1):
      binary = "0"
print(binary + sym, end="")
