# 
"""
Given a integer K. Task is Print All binary string of size K (Given number).
Examples:

Input : K = 3  
Output : 000 , 001 , 010 , 100 , 101 

Input : K  = 4 
Output :0000 0001 0010 0100 0101 1000 1001 1010   
"""

n = int(input())
a = [0] * n
def bk(k, n):
    if n == k:
        print(a)
    else:
        if a[k - 1] == 1:
            a[k] = 0
            bk(k + 1, n)
        elif a[k - 1] == 0:
            a[k] = 0
            bk(k + 1, n)
            a[k] = 1
            bk(k + 1, n)

bk(0, 3)

