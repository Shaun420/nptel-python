"""
Create a Python program to determine the nth element of an arithmetic sequence where the first term a is 7 and the common difference d is 11. The program should prompt the user to input the value of n, then compute and print the nth element of the sequence.

Input Format:
The input consists of a single integer n.

Output Format:

The output consists of the nth element of the arithmetic sequence.

Example:
Input:
3
Output:
29
"""

a = 7
d = 11
n = int(input())
print((a + ((n - 1) * d)), end="")
temp = 0