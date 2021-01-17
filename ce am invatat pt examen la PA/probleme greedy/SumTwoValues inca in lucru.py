"""
You are given an array of n integers, 
and your task is to find two values (at distinct positions) whose sum is x.

Input

The first input line has two integers n and x: the array size and the target sum.

The second line has n integers a1,a2,…,an: the array values.

Output

Print two integers: the positions of the values. If there are several solutions, 
you may print any of them. If there are no solutions, print IMPOSSIBLE.

Input:
4 8
2 7 5 1

Output:
2 4
"""

ns = [int(x) for x in input().split()]
n, x = ns[0], ns[1]
lst = [int(x) for x in input().split()]

"""
# lst = sorted(lst)
i = 0
j = len(lst) - 1
gasit = 0
while i <= j:
    if lst[i] + lst[j] > x:
        j -= 1
    elif lst[i] + lst[j] < x:
        i += 1
    else:
        gasit = 1
        break


if gasit == 0 or (i == 0 and j == 0):
    print("IMPOSSIBLE")
else:
    print(i + 1, j + 1)
"""

sortat = sorted(lst)

gasit = 0

def twoNumberSum(vector, suma):
    nums = {}
    for numar in vector:
        if suma - numar in nums:
            return (suma - numar, numar)
        else:
            nums[numar] = True
    return []

if twoNumberSum(sortat, x) != []:
    print(lst.index(twoNumberSum(sortat, x)[0]) + 1, lst.index(twoNumberSum(sortat, x)[1]) + 1)
else:
    print("IMPOSSIBLE")

# mai am niste probleme pe la alea unde s multe elemente



            



