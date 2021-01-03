# Cum verifici daca un vector contine o anumita valoare in Python

from array import *
vector = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
numar = 3

# un Divide Et Impera corespunzator

def arrayNumber(vector, numar):
    vector.sort()
    stanga = 0
    dreapta = len(vector) - 1

    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2
        if vector[mijloc] < numar:
            stanga = mijloc + 1
        elif vector[mijloc] > numar:
            dreapta = mijloc - 1
        else:
            print(mijloc)
            break


        
