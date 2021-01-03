# produsul maxim a doi intregi dintr-un vector unde toate elementele sunt pozitive

vector = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

# Idee 1 : gasesc maxim1 si maxim2 din vector, dupa care logic ca produsul maxim este maxim1*maxim2 O(n)

maxim1 = -1
maxim2 = -1

for numar in vector:
    if numar > maxim1:
        if maxim1 == -1 and maxim2 == -1:
            maxim1 = numar
            maxim2 = numar
        else:
            maxim2 = maxim1
            maxim1 = numar
    elif maxim2 < numar and numar < maxim1:
        maxim2 = numar

print((maxim2, maxim1))

# Idee 2: doua foruri si compari perechile O(n^2)

