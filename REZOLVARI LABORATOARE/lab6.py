"""
1.
Primiit o lista vida si o lista de operatii.
Executati ops:
    1: se introduce x in multime
    2: se extrage si se afiseaza cel mai mic element
"""

"""
from heapq import heappush, heappop

# heappush -> 

xs = []            # m operatii
ops = [
    (1, 1),        # xs = [1]
    (1, 5),        # xs = [1, 5]
    (1, 3),        # xs = [1, 3, 5]
    (2,),          # xs = [3, 5]     => 1
    (1, 9),        # xs = [3, 5, 9]
    (2,),          # xs = [5, 9]     => 3
    (2,),          # xs = [9]        => 5
    (1, 4),        # xs = [4, 9]
    (2,),          # xs = [9]        => 4
    (2,)           # xs = []         => 9
]    

for op in ops:
    if op[0] == 1:
        heappush(xs, op[1])
    else:
        print(heappop(xs))
"""

"""
2.
Fie multimea H = {2^x * 3^y * 5^z | x, y, z ∊ N}. Scrieti primele m elemente alte multimii.
Rezolvati problema anterioara folosind heapuri. 
Idee: se introduce primul element al multimii in heap. 
Se extrage elementul minim din heap, se introduc elemente 2*min, 3*min, 5*min in heap. 
Se continua pana cand aveti m elemente.
"""
"""
from heapq import heappush, heappop

numere = []
m = 5

heappush(numere, 1)
while len(numere) < m:
    minim = heappop(numere)
    heappush(numere, 2 * minim)
    heappush(numere, 3 * minim)
    heappush(numere, 5 * minim)

print(sorted(numere))
"""

"""
3.
Primiti N vectori sortati avand numar variabil de componente. 
Se cer primele M componente ale vectorului care reprezinta reuniunea celor N vectori din input.

Input:             Output: 0 1 1 2 3
 4 5                
 3 1 3 4
 4 2 5 10 11      
 2 1 9              
 3 0 6 10

Rezolvati problema anterioara cu heapuri. Trebuie sa faceti o interclasare a N vectori. 
Introduceti in heap primul element al fiecarui vector. 
Extrageti minimul, si introduceti in heap urmatorul element din vector.
"""

"""
from heapq import heappush, heappop

n = int(input("N ="))
m = int(input("M ="))

liste = []
lista = []

for index in range(n):
    lista = list(input("Introdu lista:").split())
    
    for index2 in range(len(lista)):
        lista[index2] = int(lista[index2])
    
    liste.append(lista)

final = []
temporar = []

for i in range(len(liste)):
    liste[i] = sorted(liste[i])

index_final = 0
while index_final < m:
    if index_final == 0:
        for i in range(len(liste)):
            heappush(temporar, liste[i][0])
    
    else:
       

"""


"""
Se considera n proiecte, pentru fiecare proiect cunoscandu-se profitul, un termen limita 
(sub forma unei zi din luna) si faptul ca implementarea sa dureaza exact o zi. 
Sa se gaseasca o modalitate de planificare a unor proiecte astfel incat profitul total sa fie maxim.

Input:
BlackFace     2     800
Test2Test     5     700
Java4All      1     150
BestJob       2     900
NiceTry       1     850
JustDoIt      3     1000
FileSeeker    3     950
OzWizard      2     900
 
Output:
Ziua 1: BestJob 900
Ziua 2: FileSeeker 950
Ziua 3: JustDoIt 1000
Ziua 5: Test2Test 700
 
Profit maxim: 3550

sortati dupa profit. Rezolvati proiectele cat mai tarziu.
"""

"""
proiecte = [
    # ['BlackFace', 1, 800],
    # ['Test2Test', 5, 700],
    # ['Java4All', 1, 150],
    # ['BestJob', 2, 900],
    # ['NiceTry', 1, 850],
    # ['JustDoIt', 3, 1000],
    # ['FileSeeker', 3, 950],
    # ['OzWizard', 2, 900]
    ["a", 1, 700],
    ["b", 2, 800],
    ["c", 3, 900]
]

def programareProiecte(proiecte, numar_zile):
    # salvam lungimea listei de proiecte
    n = len(proiecte)

    # sortez descrescator dpdv al profitului
    def sortezDescrescatorProfitului(lista):
        return lista[2]
    
    proiecte = sorted(proiecte, key=sortezDescrescatorProfitului, reverse=True)

    # fac o lista unde marchez timpii:
    timpiMarcati = [False] * numar_zile
    listaJoburi = ['-1'] * numar_zile

    for index in range(len(proiecte)):
        # gasim un loc liber pentru proiect
        # pornim de la ultimul loc posibil
        # pornesc de la index 2 care va fi minimul dintre numarul maxim de zile si ziua in care e programat
        # proiectul - 1, adica verificam daca exista zile in care nu facem absolut nimic, ca sa punem
        # un proiect cu profit mare.
        for index2 in range(min(numar_zile, proiecte[index][1] - 1), -1, -1):
            # cautam daca pe timpiMarcati[index2] gasim False, daca e False inseamna ca nu facem nimic in ziua
            # aia. Deci punem o activitate.
            if timpiMarcati[index2] == False:
                # am gasit o zi libera pentru un job.
                timpiMarcati[index2] = True
                listaJoburi[index2] = proiecte[index][0] # punem numele proiectului pe index2 care retine si timpul
                break


    for index in range(len(listaJoburi)):
        print("Ziua " + str(index + 1) + ": " + listaJoburi[index])    

programareProiecte(proiecte, 3)
"""






    
