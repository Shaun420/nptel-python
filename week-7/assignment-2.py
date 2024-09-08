"""
Question

Write a Python program that includes a recursive function named is_palindrome which takes a non-empty string s as input. The function should return 1 if the string is a palindrome (reads the same backward as forward), and 0 otherwise.

Take necessary inputs, pass the inputs to the function, and print the return value of the function.

Input Format:

The input consists of a single line containing the string s.

Output Format:

The output consists of a single integer value (1 or 0) indicating whether the string is a palindrome.

Example:

Input:
racecar

Output
1
"""

s = input()
def is_palindrome(s):
  if len(s) <= 1:
    return 1
  if s[0] != s[-1]:
    return 0
  return is_palindrome(s[1:-1])

print(is_palindrome(s), end="")
