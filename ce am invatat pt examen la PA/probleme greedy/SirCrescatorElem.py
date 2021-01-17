# Se cere cel mai lung sir strict crescator cu elemente din vectorul A = (a1, a2 .., an)
# Solutie: Incepem prin a ordona crescator elementele vectorului a (Corespunzator procedurii prel).
# Apo parcurgem vectorul de la stanga la dreapta

import sys

A = [1,1,2,3,4,4,5,6,7,8,8]
A = sorted(A)

a_curent = []
solutie = []

for i in range(len(A)):
    if i == 0:
        # Daca i e 0 n-avem nimic in subvectorul curent,deci adaugam
        a_curent.append(A[i])
    else:
        if A[i] > A[i - 1]:
            # Pentru ca vrem sa fim siguri ca sirul este strict crescator, comparam cu predecesorul
            a_curent.append(A[i])
        else:
            # Daca nu se respecta conditia, verificam subvectorul curent daca este maxim.
            if(len(a_curent)> len(solutie)):
                solutie = a_curent # Daca da, atunci am gasit solutia

            a_curent = [] # resetam vectorii si adaugam din nou elementul curent
            a_curent.append(A[i])

print(solutie)
        





