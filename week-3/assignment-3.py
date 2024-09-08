"""
Create a Python program that takes a list of integers, reverses the list, adds the values at odd indices from both the original and reversed lists, and creates a new list with the result. The new list should be printed in the end.

Input Format:
The input consists of a single list of integers, separated by spaces.

Output Format:
The output consists of the new list of values, separated by spaces, obtained by adding values at odd indices from both the original and reversed lists.

Example:
Input:
1 2 3 4 5

Output:
1 6 3 6 5
"""

list1 = input().split(" ")
list2 = []
n = len(list1)
for i in range(n):
	if (int(i) % 2 == 0):
		list2.append(list1[i])
	else:
		list2.append(str(int(list1[i]) + int(list1[n - i - 1])))
print(" ".join(list2), end="")
