"""
Create a Python program that performs a binary search on a sorted list of integers using only loops. The program should prompt the user to input a sorted list of integers and a target number to search for. The program should then search for the target number in the list using the binary search algorithm and print the index of the target if found. If the target is not found, the program should print -1.

Input Format:

    The first line of input consists of a space-separated sorted list of integers.
    The second line of input consists of a single integer, representing the target number.

Output Format:

    The output consists of the index of the target number in the list if found. If the target number is not found, the output should be -1.

Example:
Input:
10 20 30 40 50
30

Output:
2
"""

arr = list(map(int, input().split(" ")))
target = int(input())

low = 0
high = len(arr) - 1
while low <= high:
  mid = (low + high) // 2
  if (arr[mid] == target):
    print(mid, end="")
    break
  if (target < arr[mid]):
    high = mid - 1
    continue
  else:
    low = mid + 1
    continue
if arr[mid] != target:
  print(-1, end="")
