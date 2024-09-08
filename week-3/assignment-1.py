"""
Create a Python program that finds the second largest number in a list of positive integers(includes zero). The program should prompt the user to input a list of numbers, then compute and print the second largest number in that list.

Input Format:
The input consists of a single list of numbers, separated by spaces.
Hint: Use .split() function to convert input to list.

Output Format:
The output consists of the second largest number in the input list.

Example:

Input:
3 1 4 1 5 9 2 6 5 3 5

Output:
6
"""

inputstr = input()
num = inputstr.split(" ")
max1 = 0
max2 = 0
for x in num:
	x = int(x)
	if (x > max1):
		max2 = max1
		max1 = x
	elif (x < max1) and (x > max2):
		max2 = x
print(max2, end="")