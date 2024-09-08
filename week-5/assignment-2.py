"""
Create a Python program that merges two sorted lists into one sorted list. The program should prompt the user to input two sorted lists of integers. The program should then merge these two lists into one sorted list and print the result.

Input Format:
The first line of input consists of a space-separated sorted list of integers.
The second line of input consists of another space-separated sorted list of integers.

Output Format:
- The output consists of a single sorted list, which is the result of merging the two input lists.

Example:

Input:
1 3 5 7
2 4 6 8

Output:
1 2 3 4 5 6 7 8
"""

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
m = len(a)
n = len(b)
k = 0
result = []

i = j = 0
while i < m and j < n:
  if (a[i] <= b[j]):
    result.append(a[i])
    i += 1
  else:
    result.append(b[j])
    j += 1
  k += 1
while i < m:
  result.append(a[i])
  i += 1
  k += 1
while j < n:
  result.append(b[j])
  j += 1
  k += 1
print(" ".join(list(map(str, result))), end="")
