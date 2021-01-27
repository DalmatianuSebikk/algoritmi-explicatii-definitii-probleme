"""
Given a string str, the task is to print all the permutations of str. 
A permutation is an arrangement of all or part of a set of objects, 
with regard to the order of the arrangement. For instance, the words ‘bat’ and ‘tab’ represents 
two distinct permutation (or arrangements) of a similar three letter word.
"""

cuvant = input()
lista = [char for char in cuvant]
print(list)
f = [0] * len(lista)
a = [''] * len(lista)

def bk(k, n):
    if k == n:
        print(a)
    else:
        for i in range(n):
            if f[i] == 0:
                f[i] = 1
                a[k] = lista[i]
                bk(k + 1, n)
                f[i] = 0

bk(0, len(lista))