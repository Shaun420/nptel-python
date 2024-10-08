"""
Create a Python program that finds the k-th largest and k-th smallest elements in a list of integers. The program should prompt the user to input a list of integers and a value `k`. The program should then find and print:

    1 if the k-th largest and k-th smallest elements are the same and are at the middle of the sorted list.
     -1 if the k-th largest and k-th smallest elements are the same but are not in the middle of the sorted list.
    0 if the k-th largest and k-th smallest elements are different.

Input Format:

    The first line of input consists of a space-separated list of integers.
    The second line of input consists of a single integer k.

Output Format:
The output consists of a single integer 1, -1, or 0 based on the conditions specified.

Example:

Input:
3 8 7 5 9 1
2

Output:
0
"""

arr = list(map(int, input().split(" ")))
k = int(input())

arr.sort()

if arr[k-1] == arr[-k]:
  if k == len(arr)//2+1:
    print("1", end="")
  else:
    print("-1", end="")
else:
  print("0", end="")
