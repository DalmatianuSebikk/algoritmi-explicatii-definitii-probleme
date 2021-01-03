"""CERINTA"""
# Ti se da un vector cu elemente distincte. sa se verifice daca exista sau nu o pereche de numere astfel incat 
# adunate sa dea o anumita suma

#-----------------------------------------------------

# O PRIMA IDEE (O(n^2)): poti parcurge cu 2 foruri si sa verifici pentru fiecare numar daca exista un altul diferit de el
# in lista care sa dea suma cautata.

# O A DOUA IDEE mai eficienta decat prima (O(n*logn)): Sortarea vectorului si folosirea pointerilor.
# Mergem cu 2 pointeri (L - inceput, R - final) si ii adunam. Daca suma este mai mica decat cea cautata,
# atunci mergem cu pointerul din stanga cu o pozitie la dreapta. Altfel, daca suma este mai mare, 
# mergem cu pointerul din dreapta cu o pozitie la stanga

# O ALTA IDEE --MAI EFICIENTA--: Folosirea Hash-table -urilor. 
# Nu va iesi eficient din punct de vedere al spatiului

"""
----
targetSum = 10
currentNum = x
----
Trebuie sa gasim un numar y astfel incat x + y = 10 => y = 10 - x
Daca y este in hash-table atunci returnam x si y. Altfel, continuam sa traversam lista si nu uitam
sa il adaugam pe x in hash-table

EX:
fie lista = [3, 5, -4, 8, 11, 1, -1, 6] si suma = 10.
-----------
currentNum = 3. y = 7. Este 7 in hash-table? Nu. Dar il adaugam pe x in Hash-table.
currentNum = 5. y = 5. Este 5 in hash-table? Nu. Dar il adaugam pe x in Hash-table.
...............
currentnum = -1. y = 11. Este 11 in hash-table? Da, pentru ca l-am vazut mai inainte. Deci returnam 11, -1.
GATA

"""

# IMPLEMENTARE

# PRIMA IDEE: O(n^2)
"""
vector = [3, 5, -4, 8, 11, 1, -1, 6]
suma = 10
print(vector)

def twoNumberSum(vector, suma):
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i] + vector[j] == suma:
                return (vector[i], vector[j])

print(twoNumberSum(vector, suma))
"""

# A DOUA IDEE: O(n*logn) si O(1) ca spatiu
"""
vector = [3, 5, -4, 8, 11, 1, -1, 6]
suma = 10

def twoNumberSum(vector, suma):
    vector.sort()
    print(vector)

    #punem pointerii
    pl = 0
    pr = len(vector) - 1

    while pl < pr:
        if vector[pl] + vector[pr] < suma:
            pl += 1
        elif vector[pl] + vector[pr] > suma:
            pr -= 1
        else:
            return (vector[pl], vector[pr])

print(twoNumberSum(vector, suma))
"""

# A TREIA IDEE: O(n)

"""
vector = [3, 5, -4, 8, 11, 1, -1, 6]
suma = 10

def twoNumberSum(vector, suma):
    nums = {}
    for numar in vector:
        if suma - numar in nums:
            return (suma - numar, numar)
        else:
            nums[numar] = True
    return []

print(twoNumberSum(vector, suma))
"""


