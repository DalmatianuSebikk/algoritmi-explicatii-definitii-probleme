# algoritmii au aceeasi dimensiune la datele de intrare

# Big O - limbajul si metrica folosita pentru a descrie eficienta unui algoritm

# BIG O, BIG THETA SI BIG OMEGA

# Big O - complexitatea mai mica sau egala cu cea mai rea
# Big Omega - complexitatea cea mai buna
# Big Theta - complexitatea dintre cea mai buna si cea mai rea complexitate

# EXEMPLE DE COMPLEXITATI:
#   - O(1) -> Constant, Accesarea unui element specific dintr un vector (vector[i]) (Bun)
#   - O(n) -> Linear, Un loop prin elementele unui vector (Nu chiar asa de bun, e ok)
#   - O(logN) -> Logaritmic, Gasirea unui element intr-un vector sortat (Bun)
#   - O(N^2) -> Quadratic, 2 foruri (Oribil)
#   - O(2^n) -> Exponential, Recursie dubla in Fibonacci (Mamma mia)

# COMPLEXITATEA SPATIULUI:
# - cat spatiu consuma programul

# - Daca faci un vector de n elemente atunci ai complexitatea spatiului O(n)
# - Daca ai o matrice de n*n elemente atunci ai complexitatea spatiului O(n^2)

# EXEMPLU PENTRU RECURSIVITATE:
"""
def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n - 1)
"""

# Blocul asta de cod face suma lui Gauss. Pe stiva programului va adauga numerele de la 1 la n, deci complexitatea
# spatiului va fi O(n)

# EXEMPLU DE COMPLEXITATE O(1)
"""
def sumePare(n):
    suma = 0
    for i in range(0, n + 1):
        suma = suma + pereche(i, i + 1)
    return suma

def pereche(a, b):
    return a + b

print(sumePare(4))
"""

# Complexitatea spatiului este O(1) pentru ca nu foloseste vectori


# SUME SI INMULTIRI 

# Daca de exemplu ai 2 foruri (nu unul in altul):
"""
for a in vectorA:
    print(a)

for b in vectorB:
    print(b)
"""
# Atunci avem complexitatea O(len(vectorA) + len(vectorB))

# Daca avem 2 foruri unul in altul:
"""
for a in vectorA:
    for b in vectorB:
        print(a, b)
"""
# Atunci avem complexitatea O(len(vectorA) * len(vectorB))