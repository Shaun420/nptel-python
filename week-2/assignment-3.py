"""
Create a Python program to compute the sum of the first N natural numbers {1,2,3...N}. The program should prompt the user to input the value of N, then compute and print the sum of the first N natural numbers.

Input Format:
The input consists of a single integer N.

Output Format:
The output consists of the sum of the first N natural numbers.

Example:
Input-
5
Output-
15
"""

temp = 0
n = int(input())
print(int(n * (n + 1) / 2), end="")
temp = 0
