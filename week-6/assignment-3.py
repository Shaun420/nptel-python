"""
Question
Write a Python program that includes a recursive function named non_decreasing which takes a non-empty list L of integers as input. The function should return True if the elements in the list are sorted in non-decreasing order from left to right, and False otherwise.

Input Format:
The input consists of a single line containing space-separated integers that form the list L.

Output Format:
The output consists of a single boolean value (True or False) indicating whether the list is sorted in non-decreasing order.

Example:

Input:
1 2 2 3 4

Output:
True
"""

inputlist = input().split(" ")
L = list(map(int, inputlist))

def non_decreasing(L, i = 1):
  if (i == 0):
    return False
  if (i == len(L)):
    return True
  if (L[i] < L[i - 1]):
    return False
  else:
    return non_decreasing(L, i + 1)

print(non_decreasing(L), end="")
