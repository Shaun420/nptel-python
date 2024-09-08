"""
Create a Python program that calculates the absolute value of a given number.
The program should prompt the user to input a number, then compute and print the absolute value of that number.

Input Format-
The input consists of single number.

Output Format-
The output consists of absolute value of the input.

Example-
Input:
-6
Output:
6
"""

temp = 0
n = int(input())
if (n < 0):
  print(-n, end="")
else:
  print(n, end="")
temp = 1