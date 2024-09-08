"""
Question:
Write a Python program that takes two positive integers a and b as input and returns their product using a recursive function. The function should only use the + and - operators to calculate the product.

Input Format:
The first line of input consists of two space-separated positive integers, a and b.

Output Format:
The output consists of a single integer representing the product of a and b.

Example:

Input:
3 4

Output:
12
"""

inputlist = input().split(" ")
a = int(inputlist[0])
b = int(inputlist[1])

def multiply(a, b):
  if b == 0:
    return 0
  if b == 1:
    return a
  else:
    return a + multiply(a, b - 1)

print(multiply(a, b), end="")
