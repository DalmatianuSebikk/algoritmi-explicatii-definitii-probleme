# 1. Sortati numerele dintr-o lista folosind bubble sort. 
# In aceasta sortare parcurgem numerele si daca se afla intr-o pozitie gresita
# (nr mare in dreapta, nr mic in stanga), le interschimbam. Continuam sa facem aceste parcurgeri cat 
# timp au inca loc interschimbari. Daca intre doua parcurgeri nu au avut loc interschimbari, ne oprim.

"""
vector = [5, 4, 3, 2, 1]

for i in range(len(vector)):
    for j in range(len(vector) - 1):
        if vector[j] > vector[i]:
            aux = vector[j]
            vector[j] = vector[i]
            vector[i] = aux

print(vector)
"""
"""
vector = [5, 4, 3, 2, 1]

not_sortat = True

while(not_sortat):
    not_sortat = False
    for i in range(len(vector) - 1):
        if vector[i] > vector[i + 1]:
            aux = vector[i]
            vector[i] = vector[i + 1]
            vector[i + 1] = aux
            not_sortat = True

print(vector)
"""

# 2. Sortati numerele dintr-o lista folosind insertion sort. 
# Presupunem ca primele k elemente sunt sortate. Consideram elementul k+1 si il inseram 
# la locul potrivit printre primele k elemente (mutand celelalte elemente la dreapta).

"""
xs = [1,5,2,7,4,9,10,0,8]

for i in range(1, len(xs)): # pornim de la elementul al doilea ca sa putem lua key ul corect
    cheie = xs[i]
    j = i - 1 # mutam elementele de pe pozitiile [0 ... i - 1] care s mai mari decat cheie cu o poz mai incolo

    while j >= 0 and cheie < xs[j]:
        xs[j + 1] = xs[j]
        j -= 1

    xs[j + 1] = cheie

print(xs)
"""

# 3. Sortati numerele dintr-o lista folosind selection sort folosind selectia minimului. 
# Parcurgem vectorul, gasim minimul si il punem pe prima pozitie. 
# Cautam urmatorul minim (intre 1 si n-1) il punem pe a doua pozitie s.a.m.d.

"""
xs = [1,5,2,7,4,9,10,0,8]



def minim(lista, de_la_cat_pornesc):
    minimul = lista[de_la_cat_pornesc]
    for i in range(de_la_cat_pornesc, len(lista)):
        if lista[i] <= minimul:
            minimul = lista[i]
    return minimul

i = 0
while i < len(xs):
    minTemp = minim(xs, i)
    poz = xs.index(minTemp)

    aux = xs[i]
    xs[i] = xs[poz]
    xs[poz] = aux

    i += 1

print(xs)
"""

# 4. Sortati numerele dintr-o lista folosind merge sort. Trebuie sa scrieti algoritmul de interclasare care 
# primeste doua liste sortate crescator si returneaza o lista sortata care contine toate elementele 
# celor doua liste.
# Aplicati apoi algoritmul merge sort: Cat timp vectorul are o lungime mai mare decat 1, 
# impartim vectorul in doua parti egale (sau aproximativ egale), 
# folosim merge_sort pe cele doua parti, dupa cele doua apeluri avem doi vectori sortati, 
# aplicam interclasarea si returnam vectorul rezultat.

"""
xs = [1,5,2,7,4,9,10,0,8]

def interclasare(lista1, lista2, lista3):
    pozLista1 = 0
    pozLista2 = 0
    index = 0

    while pozLista1 < len(lista1) and pozLista2 < len(lista2):
        if lista1[pozLista1] < lista2[pozLista2]:
            lista3[index] = lista1[pozLista1]
            pozLista1 += 1
        else:
            lista3[index] = lista2[pozLista2]
            pozLista2 += 1
        index += 1

    while pozLista1 < len(lista1):
        lista3[index] = lista1[pozLista1]
        pozLista1 += 1
        index += 1

    while pozLista2 < len(lista2):
        lista3[index] = lista2[pozLista2]
        pozLista2 += 1
        index += 1

def mergeSort(lista):
    if len(lista) > 1:

        mijloc = len(lista) // 2
        stanga = lista[:mijloc]
        dreapta = lista[mijloc:]

        mergeSort(stanga)
        mergeSort(dreapta)

        # interclasare
        interclasare(stanga, dreapta, lista)

        


mergeSort(xs)
print(xs)
"""

# 5.Sortati numerele dintr-o lista folosind quick sort. 
# Trebuie sa alegeti un pivot (de exemplu primul element), sa gasiti numerele mai mici, 
# egale si mai mari decat pivotul, si returnati quick_sort(mai_mici) + egale + quick_sort(mai_mari). 
# Puteti folosi list comprehension daca vreti ([x for x in xs if x < p]).

"""
xs = [1,5,2,7,4,9,10,0,8]

def partitie(lista, stanga, dreapta):
    i = stanga - 1
    pivot = lista[dreapta]

    for j in range(stanga, dreapta):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i] #SWAP
    
    lista[i + 1], lista[dreapta] = lista[dreapta], lista[i + 1] #SWAP

    return (i + 1)

def quickSort(lista, stanga, dreapta):
    if stanga < dreapta:
        index_partitie = partitie(lista, stanga, dreapta)
        quickSort(lista, stanga, index_partitie - 1)
        quickSort(lista, index_partitie + 1, dreapta)

quickSort(xs, 0, len(xs) - 1)
print(xs)
"""

# Simulati o coada folosind doua stive. 
# Primiti operatii uzuale pentru cozi (inserare la sfarsit, stergere de la inceput). 
# Simulati operatiile pe acea coada folosind doua stive. Afisati lista operatiilor pentru cele doua stive 
# in urmatorul format:
# 0 0 x => pe stiva 0, aplicam operatia de inserare (0) pentru x
# 1 0 x => pe stiva 1, aplicam operatia de inserare (0) pentru x
# 0 1 1 => de pe stiva 0, extragem elementul (1) si il inseram in 1
# 1 1 0 => de pe stiva 1, extragem elementul (1) si il inseram in 0
# 0 2 => se extrage elementul din stiva 0
# 1 2 => se extrage elementul din stiva 1

# 0-> append
# 1-> pop si append
# 2-> pop

"""
coada = []
stiva1 = []
stiva2 = []

operatii = [
    (0, 0, 4),
    (0, 0, 5),
    (0, 0, 6),

    (0, 1, 1),
    (0, 1, 1),
    (0, 1, 1),

    (1, 2),
    (1, 2),
    (1, 2)
]

for operatie in operatii:
    if len(operatie) == 3:
        if operatie[0] == 0:
            if operatie[1] == 0: # e append
                stiva1.append(operatie[2])
            elif operatie[1] == 1 and operatie[2] == 1:
                stiva2.append(stiva1.pop())

        elif operatie[0] == 1:
            if operatie[1] == 0:
                stiva2.append(operatie[2])
            elif operatie[1] == 1 and operatie[2] == 0:
                stiva1.append(stiva2.pop())

    else:
        if operatie[0] == 0 and operatie[1] == 2:
            coada.append(stiva1.pop())
        elif operatie[0] == 1 and operatie[1] == 2:
            coada.append(stiva2.pop())

print(coada)
"""

# Primiti n numere naturale si un numar s. 
# Trebuie sa afisati daca puteti alege exact 6 numere (nu neaparat distincte) astfel incat 
# suma lor sa fie s. Daca nu se poate afisati -1.

# Metoda meet in the middle

suma_data = 13
lista = [1, 2, 3, 4, 5, 6]

# formam lista de tupluri de cate 3 



# consideram toate tuplurile care pot fi formate cu elementele listei
tupluri = []
for numar in lista:
    for numar2 in lista:
        for numar3 in lista:
            tupluri.append((numar, numar2, numar3))


# sortam elementele listei de tupluri dupa suma elementelor din tuplu
def suma(tuplu):
    return tuplu[0] + tuplu[1] + tuplu[2]

tupluri = sorted(tupluri, key=suma)

# cautam binar alte elemente unde suma(tuplu cautat) + suma(tuplu insumat) sa dea numarul dat
def cautare_binara(tupluri, stanga, dreapta, insumat):
    if stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2

        if suma(tupluri[mijloc]) + suma(insumat) == suma_data:
            return tupluri[mijloc]
        
        elif suma(tupluri[mijloc]) + suma(insumat) > suma_data:
            return cautare_binara(tupluri, mijloc + 1, dreapta, insumat)
        
        else:
            return cautare_binara(tupluri, stanga, mijloc - 1, insumat)

    else:
        return -1

# trecem prin fiecare element din vector si verificam daca gasim, ca daca gasim oprim executia
for tuplu in tupluri:
    rezultat = cautare_binara(tupluri, 0, len(tupluri) - 1, tuplu)
    if rezultat != -1:
        print(tuplu)
        print(rezultat)
        break

if rezultat == -1:
    print(rezultat)











