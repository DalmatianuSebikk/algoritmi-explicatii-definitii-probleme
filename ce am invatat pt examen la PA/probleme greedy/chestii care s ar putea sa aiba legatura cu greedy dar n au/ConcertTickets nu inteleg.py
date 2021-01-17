"""
There are n concert tickets available, each with a certain price. 
Then, m customers arrive, one after another.

Each customer announces the maximum price he or she is willing to pay for a ticket, 
and after this, they will get a ticket with the nearest possible price such that 
it does not exceed the maximum price.

Input

The first input line contains integers n and m: the number of tickets and the number of customers.

The next line contains n integers h1,h2,…,hn: the price of each ticket.

The last line contains m integers t1,t2,…,tm: the maximum price for each customer.

Output

Print, for each customer, the price that they will pay for their ticket.
After this, the ticket cannot be purchased again.

If a customer cannot get any ticket, print −1.

Input:
5 3
5 3 7 8 5
4 8 3

Output:
3
8
-1
"""
# nush sa o fac ca nu mi da nimic cum trebuie, ca nu poti face multiset in python

import bisect # bisect_left este lowerbound si bisect_right este higherbound

# bisect_left -> The leftmost index to insert, so list remains sorted
# bisect_right -> the rightmost ____||_____

l = [int(x) for x in input().split()]
n, m = l[0], l[1]
tickets = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]

tickets = sorted(tickets)

print(tickets)

for price in prices:
    if bisect.bisect_left(tickets, price) == 0:
        print(-1)
    else:
        print(tickets[bisect.bisect_left(tickets, price) - 1])# ?
        tickets.pop(bisect.bisect_left(tickets, price)) # ?


        





