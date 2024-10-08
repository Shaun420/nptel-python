"""
Question:
Write a Python program that takes a positive integer x as input and returns the logarithm of x to the base 2 using a recursive function. The logarithm of x to the base 2, denoted by log₂(x), is the number of times 2 has to be multiplied by itself to get x. Assume that x is a power of 2.

Input Format:
The input consists of a single positive integer x which is a power of 2.

Output Format:
The output consists of a single integer representing log₂(x).

Example:

Input:
8

Output:
3
"""

x = int(input())

def logbase2(required, i = 0):
  if (required == 2**i):
    return i
  return logbase2(required, i + 1)

print(logbase2(x), end="")
