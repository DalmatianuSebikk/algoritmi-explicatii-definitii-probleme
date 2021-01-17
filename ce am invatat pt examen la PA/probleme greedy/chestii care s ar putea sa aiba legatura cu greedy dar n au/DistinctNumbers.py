"""
You are given a list of n integers, 
and your task is to calculate the number of distinct values in the list.

The first input line has an integer n: the number of values.

The second line has n integers x1,x2,…,xn.

5
2 3 2 2 3

2
"""
n = int(input())
xs = input().split()
xs = [int(x) for x in xs]

k = 0
d = {}

for element in xs:
    if element not in d:
        d[element] = 1
        k+= 1

print(k)




