"""
You are given the arrival and leaving times of n customers in a restaurant.

What was the maximum number of customers?

Input

The first input line has an integer n: the number of customers.

After this, there are n lines that describe the customers. 
Each line has two integers a and b: the arrival and leaving times of a customer.

You may assume that all arrival and leaving times are distinct.

Output

Print one integer: the maximum number of customers.

Input:
3
5 8
2 4
3 9

Output:
2
"""

# NU e asemanatoare cu activity selection, de ce vor elementul comun
# am considerat 1 element din stanga si -1 element din dreapta
# si acum facem problema cu suma maxima
n = int(input())
l_arrive_leaving = []

for i in range(n):
    da = [int(x) for x in input().split()]
    x, y = da[0], da[1]
    l_arrive_leaving.append((x, 1))
    l_arrive_leaving.append((y, -1))

l_arrive_leaving = sorted(l_arrive_leaving)
sum = 0
ans = 0

for tupla in l_arrive_leaving:
    sum += tupla[1]
    ans = max(ans, sum)
    

print(ans)




