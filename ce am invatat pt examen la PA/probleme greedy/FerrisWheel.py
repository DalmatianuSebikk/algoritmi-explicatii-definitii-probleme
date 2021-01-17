"""
There are n children who want to go to a Ferris wheel, and your task is to find a gondola for each child.

Each gondola may have one or two children in it, and in addition, the total 
weight in a gondola may not exceed x. You know the weight of every child.

What is the minimum number of gondolas needed for the children?

Input

The first input line contains two integers n and x: 
the number of children and the maximum allowed weight.

The next line contains n integers p1,p2,…,pn: the weight of each child.

Output

Print one integer: the minimum number of gondolas.

Input:
4 10
7 2 3 9

Output:
3
"""

numere = [int(x) for x in input().split()]
n, x = numere[0], numere[1]
weights = [int(x) for x in input().split()]

weights = sorted(weights)
# sortez crescator si iau cate 2, unul de la inceput, unul de la final, cu 2 pointeri ma duc eventual
ans = 0
i = 0
j = len(weights) - 1

while i <= j:
    if weights[i] + weights[j] > x:
        j -= 1
    else:
        i += 1
        j -= 1
    
    ans += 1

print(ans)

