"""
Given a positive integer number N. 
The task is to generate all the binary strings of N bits. 
These binary strings should be in ascending order.

Input: 2
Output:
0 0
0 1
1 0
1 1

Input: 3
Output:
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1

"""
global n
n = int(input())
a = [0]*n

def bk(k, n):
    if n == k:
        print(a)
    else:
        for i in range(2):
            a[k] = i
            bk(k + 1, n)

bk(0, n)